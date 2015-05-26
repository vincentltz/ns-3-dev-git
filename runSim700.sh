
FILES=~/randomTopology/Net_700_*

for f in $FILES
do

	echo $f
	#./waf
	./waf --run "topoTestAdhoc --infile="$f" --outHopsFile=scratch/maxhopscmd_700.txt --outTimeFile=scratch/maxtimecmd_700.txt --outAvgMsgFile=scratch/avgmsgcmd_700.txt"
done
