
FILES=~/randomTopology/Net_1300_*

for f in $FILES
do

	echo $f
	#./waf
	./waf --run "topoTestAdhoc --infile="$f" --outHopsFile=scratch/maxhopscmd_1300.txt --outTimeFile=scratch/maxtimecmd_1300.txt --outAvgMsgFile=scratch/avgmsgcmd_1300.txt"
done
