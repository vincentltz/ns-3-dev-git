
FILES=~/randomTopology/Net_250_*

for f in $FILES
do

	echo $f
	#./waf
	./waf --run "topoTestAdhoc --infile="$f" --outHopsFile=scratch/maxhopscmd_250.txt --outTimeFile=scratch/maxtimecmd_250.txt --outAvgMsgFile=scratch/avgmsgcmd_250.txt"
done
