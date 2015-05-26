/* -*- Mode:C++; c-file-style:"gnu"; indent-tabs-mode:nil; -*- */
 /*
 * Copyright (c) 2015 Tingzhi Li
 *
 * This program is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License version 2 as
 * published by the Free Software Foundation;
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program; if not, write to the Free Software
 * Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
 *
 * Author: Tingzhi Li <vincentltz at gmail dot com>
 */

#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
#include <cstdlib>
#include <typeinfo>
#include <time.h>
#include <unistd.h>
#include <math.h>

#include "ns3/object.h"
#include "ns3/core-module.h"
#include "ns3/network-module.h"
#include "ns3/internet-module.h"
#include "ns3/applications-module.h"
#include "ns3/global-route-manager.h"
#include "ns3/mobility-module.h"
#include "ns3/assert.h"

#include "ns3/wifi-module.h"
#include "ns3/config-store-module.h"
#include "ns3/olsr-helper.h"
#include "ns3/ipv4-static-routing-helper.h"
#include "ns3/ipv4-list-routing-helper.h"

#include "ns3/gossip-generator.h"
#include "ns3/gossip-generator-helper.h"

using namespace std;
using namespace ns3;

NS_LOG_COMPONENT_DEFINE ("GenericTopologyCreation");

class simstats {
    double time;
    int hops;
    double avgMsg;
  public:
    simstats(double, int, double);
    int getHops(void);
    double getTime(void);
    double getAvgMsg(void);
}; 

simstats::simstats (double t, int h, double msg) {
    time = t;
    hops = h;
    avgMsg = msg;
}

int simstats::getHops(void){
    return hops;
}

double simstats::getTime(void){
    return time;
}

double simstats::getAvgMsg(void){
    return avgMsg;
}

Ptr<GossipGenerator> GetGossipApp(Ptr <Node> node) {
    Ptr<Application> gossipApp = node->GetApplication (0) ;
    return DynamicCast<GossipGenerator>(gossipApp);
}

simstats simulation(char *filename) {
    NS_LOG_INFO ("Filename : " << filename << " to read from for  GossipGenerator");
    
    std::string phyMode ("DsssRate1Mbps");
    double distance = 5; // m
    //double rss = -20; // dBm

    NodeContainer nodes;
    NetDeviceContainer devices;
    Ipv4InterfaceContainer interfaces;
    
    WifiHelper wifi;
    InternetStackHelper stack;
    Ipv4AddressHelper ipv4;
    
    // disable fragmentation for frames below 2200 bytes
    Config::SetDefault ("ns3::WifiRemoteStationManager::FragmentationThreshold", StringValue ("2200"));
    // turn off RTS/CTS for frames below 2200 bytes
    //Config::SetDefault ("ns3::WifiRemoteStationManager::RtsCtsThreshold", StringValue ("2200"));
    // Fix non-unicast data rate to be the same as that of unicast
    Config::SetDefault ("ns3::WifiRemoteStationManager::NonUnicastMode",
                        StringValue (phyMode));
    
    wifi.SetStandard (WIFI_PHY_STANDARD_80211b);
    
    YansWifiPhyHelper wifiPhy =  YansWifiPhyHelper::Default ();
    // This is one parameter that matters when using FixedRssLossModel
    // set it to zero; otherwise, gain will be added
    wifiPhy.Set ("RxGain", DoubleValue (0) );
    
    YansWifiChannelHelper wifiChannel;
    wifiChannel.SetPropagationDelay ("ns3::ConstantSpeedPropagationDelayModel");
    
    //wifiChannel.AddPropagationLoss ("ns3::FixedRssLossModel", "Rss", DoubleValue(rss));
    wifiChannel.AddPropagationLoss ("ns3::FriisPropagationLossModel");
    wifiPhy.SetChannel (wifiChannel.Create ());
    
    // Add a non-QoS upper mac, and disable rate control
    NqosWifiMacHelper wifiMac = NqosWifiMacHelper::Default ();
    wifi.SetRemoteStationManager ("ns3::ConstantRateWifiManager",
                                  "DataMode",StringValue (phyMode),
                                  "ControlMode",StringValue (phyMode));
    // Set it to adhoc mode
    wifiMac.SetType ("ns3::AdhocWifiMac");

    GossipGeneratorHelper ggh;
    Time GossipInterval = Seconds(.005); // Must be larger than the round-trip-time! (c.f. LinkDelay)
    Time SolicitInterval = Seconds(5); // Should be larger than the GossipInterval!
    ApplicationContainer nodeApps; // TODO unused

    /* Parser Code - Begin */
    int NodeNumber, Edge1, Edge2;
    bool ParseNodes = false;
    bool ParseEdges = false;
    string Line;
    string NodePrefix = "#Nodes";
    string EdgePrefix = "#Edges";
    ifstream Topology;

    Topology.open (filename);
    while(getline(Topology,Line)) {
        if (!Line.compare(0, NodePrefix.size(), NodePrefix)) {
            ParseNodes = true;
            continue;
        }
        if (!Line.compare(0, EdgePrefix.size(), EdgePrefix)) {
            ParseNodes = false;
            NS_LOG_INFO ("Create " << NodeNumber << " nodes to test GossipGenerator");
            nodes.Create(NodeNumber);
            NS_LOG_INFO ("Install Internet Stack and GossipGenerator to those nodes.");
            devices = wifi.Install(wifiPhy, wifiMac, nodes);
           
	    int width = sqrt(NodeNumber); 
            MobilityHelper mobility;
            mobility.SetPositionAllocator ("ns3::GridPositionAllocator",
                                           "MinX", DoubleValue (0.0),
                                           "MinY", DoubleValue (0.0),
                                           "DeltaX", DoubleValue (distance),
                                           "DeltaY", DoubleValue (distance),
                                           "GridWidth", UintegerValue (width),
                                           "LayoutType", StringValue ("RowFirst"));
            mobility.SetMobilityModel ("ns3::ConstantPositionMobilityModel");
            mobility.Install (nodes);
	    /*
            // Enable OLSR
            OlsrHelper olsr;
            Ipv4StaticRoutingHelper staticRouting;
            
            Ipv4ListRoutingHelper list;
            list.Add (staticRouting, 0);
            list.Add (olsr, 10);
            
            stack.SetRoutingHelper (list); // has effect on the next Install ()
            */
            /*
            MobilityHelper mobility;
            Ptr<ListPositionAllocator> positionAlloc = CreateObject<ListPositionAllocator> ();
            positionAlloc->Add (Vector (0.0, 0.0, 0.0));
            positionAlloc->Add (Vector (5.0, 0.0, 0.0));
            mobility.SetPositionAllocator (positionAlloc);
            mobility.SetMobilityModel ("ns3::ConstantPositionMobilityModel");
            mobility.Install (nodes);
            */
            stack.Install (nodes);
            
            NS_LOG_INFO ("Assign IP Addresses.");
            ipv4.SetBase ("10.1.0.0", "255.255.0.0");
            interfaces = ipv4.Assign (devices);
            nodeApps = ggh.Install(nodes);

            NS_LOG_INFO ("Assign Addresses to Nodes and Create Links Between Nodes...");
            ParseEdges = true;
            continue;
        }
        if (ParseNodes) {
            istringstream(Line) >> NodeNumber; // Just update till end
            NodeNumber++; // convert max_index -> length
        }
        if (ParseEdges) { // Format: (12, 14)
            istringstream(Line.substr(1)) >> Edge1;
            istringstream(Line.substr(1+Line.find(","))) >> Edge2;

            NS_LOG_INFO("Parsed Edge: (" << Edge1 << ", " << Edge2 << ")");

            //Ipv4InterfaceContainer InterfaceCont = ipv4.Assign (p2p.Install (NodeContainer (nodes2.Get (Edge1), nodes2.Get(Edge2))));
            //ipv4_n.NewNetwork ();
            GetGossipApp(nodes.Get(Edge1))->AddNeighbor(interfaces.GetAddress(0),interfaces.GetAddress(1));
            GetGossipApp(nodes.Get(Edge2))->AddNeighbor(interfaces.GetAddress(1),interfaces.GetAddress(0));
        }
    }
    Topology.close();
    /* Parser Code - End */

    for ( int i=0; i<NodeNumber;++i) { //TODO use attributes
        Ptr<GossipGenerator> ii = GetGossipApp(nodes.Get(i));
        ii->SetGossipInterval(GossipInterval);
        ii->SetSolicitInterval(SolicitInterval);
    }

    Ptr<GossipGenerator> a = GetGossipApp(nodes.Get(0));
    a->SetCurrentValue( 2 );
    //a->SendMessage_debug( src,dest, TYPE_ACK );

    Simulator::Run ();

    NS_LOG_INFO(endl << " ---- Print results ---" << endl);
    int MaxHops = 0;
    Time MaxTime = Seconds(0);
    double AvgMessagesPerNode = 0;
    for ( int i=0; i<NodeNumber;++i) {
        Ptr<GossipGenerator> ii = GetGossipApp(nodes.Get(i));
        if (MaxHops < ii->GetPacketHops()){
            MaxHops = ii->GetPacketHops();
        }
        if (MaxTime.Compare(ii->GetReceivedDataTime()) == -1){
            MaxTime = ii->GetReceivedDataTime();
        }
        AvgMessagesPerNode += ii->GetSentMessages();
        NS_LOG_INFO("Node " << i << ": ");
        NS_LOG_INFO(" * Sent icmp messages   : " << ii->GetSentMessages());
        NS_LOG_INFO(" * Hops of data message : " << ii->GetPacketHops());
        NS_LOG_INFO(" * Time of data received: " << ii->GetReceivedDataTime().GetSeconds() << "s");
    }
    AvgMessagesPerNode /= NodeNumber;
    NS_LOG_INFO(endl << "Simulation terminated after " << Simulator::Now().GetSeconds() << "s");
    NS_LOG_INFO("Max hops: " << MaxHops);
    NS_LOG_INFO("Average amount of sent messages per node: " << AvgMessagesPerNode);
    NS_LOG_INFO("Time until information was spread: " << MaxTime.GetSeconds() << "s" << endl);
    simstats ret(MaxTime.GetSeconds(),MaxHops,AvgMessagesPerNode);
    Simulator::Destroy ();
    return ret;
}

/* 

  function converts std::string types into char * types
  @param string
  @return char *

*/
char* convertStrToChar(std::string str){
    char *newChars = new char[str.size()+1];
    newChars[str.size()]='\0';
    memcpy(newChars,str.c_str(),str.size());
    return newChars;
}

int main(int argc, char *argv[]) {
    // LogComponentEnable ("GossipGeneratorApplication", LOG_LEVEL_INFO);
    LogComponentEnable ("GenericTopologyCreation", LOG_LEVEL_INFO);
    // LogComponentEnable ("Icmpv4L4Protocol", LOG_LEVEL_INFO);

    srand(time(NULL));

    //These are the default values for the command line
    // if you do not override them via n3 command lines, this is what will run
    std::string inTopologyFile = "scratch/TopologyFile"; //default filenames
    std::string outHopsFile = "scratch/maxhops.txt";
    std::string outTimeFile = "scratch/maxtime.txt";
    std::string outAvgMsgFile = "scratch/avgmsg.txt";

    //This lets you add command line arguments in ns-3
    // to view all command line arguments when you run the program type:
    // ./waf --run "topoTest --help"
    //
    // it will run on the defaults provided above if no command line arguments are given
    //
    // otherwise type in :
    // ./waf --run "topoTest --infile=scratch/TopologyFile --outHopsFile=scratch/maxhops.txt --outTimeFile=scratch/maxtime.txt --outAvgMsgFile=scratch/avgmsg.txt"
    // changing the file names to what you want them to be
    // be sure to include the path!
    CommandLine cmd;
    cmd.AddValue("infile", "Topology file read in", inTopologyFile);
    cmd.AddValue("outHopsFile", "Filename that max hops are written out to", outHopsFile);
    cmd.AddValue("outTimeFile", "Filename that max hops are written out to", outTimeFile);
    cmd.AddValue("outAvgMsgFile", "Filename that avg number of messages per node are written out to", outAvgMsgFile);
    cmd.Parse (argc, argv);

    //All of the functions take char * not strings
    //but ns-3 doesn't have command line entries for char * so they need to be converted from string to char *
    char *newTopoFile = convertStrToChar(inTopologyFile);
    char *newHopsFile = convertStrToChar(outHopsFile);
    char *newTimeFile = convertStrToChar(outTimeFile);
    char *newAvgMsgFile = convertStrToChar(outAvgMsgFile);

    //makes sure nothing weird happened in conversion. comment out or delete later
    std::cout << "Filenames chars *:" << newTopoFile << " " << newHopsFile << " " << newTimeFile << " " << newAvgMsgFile << endl;

    FILE *timefile;
    FILE *hopfile;
    FILE *avgfile;
    timefile = fopen(newTimeFile, "a+");
    hopfile = fopen(newHopsFile, "a+");
    avgfile = fopen(newAvgMsgFile, "a+");

    if (timefile != NULL && hopfile != NULL && avgfile != NULL){
      for (int i = 0; i < 1; i++){
        simstats results = simulation(newTopoFile);
        fprintf(timefile,"%f\n", results.getTime());
        fprintf(hopfile,"%d\n", results.getHops());
        fprintf(avgfile,"%f\n", results.getAvgMsg());
        sleep(1);
      }
    }
    fclose(timefile);
    fclose(hopfile);
    fclose(avgfile);
    return 0;
} 
