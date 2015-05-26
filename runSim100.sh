
FILES=~/randomTopology/Net_100_*

for f in $FILES
do

	echo $f
	./waf --run "topoTestAdhoc --infile="$f" --outHopsFile=scratch/maxhopscmd_100.txt --outTimeFile=scratch/maxtimecmd_100.txt --outAvgMsgFile=scratch/avgmsgcmd_100.txt"
done
