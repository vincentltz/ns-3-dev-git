
FILES=~/randomTopology/Net_1600_*

for f in $FILES
do

	echo $f
	#./waf
	./waf --run "topoTestAdhoc --infile="$f" --outHopsFile=scratch/maxhopscmd_1600.txt --outTimeFile=scratch/maxtimecmd_1600.txt --outAvgMsgFile=scratch/avgmsgcmd_1600.txt"
done
