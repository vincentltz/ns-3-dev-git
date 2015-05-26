
FILES=~/randomTopology/Net_850_*

for f in $FILES
do

	echo $f
	#./waf
	./waf --run "topoTestAdhoc --infile="$f" --outHopsFile=scratch/maxhopscmd_850.txt --outTimeFile=scratch/maxtimecmd_850.txt --outAvgMsgFile=scratch/avgmsgcmd_850.txt"
done
