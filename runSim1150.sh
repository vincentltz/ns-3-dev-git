
FILES=~/randomTopology/Net_1150_*

for f in $FILES
do

	echo $f
	#./waf
	./waf --run "topoTestAdhoc --infile="$f" --outHopsFile=scratch/maxhopscmd_1150.txt --outTimeFile=scratch/maxtimecmd_1150.txt --outAvgMsgFile=scratch/avgmsgcmd_1150.txt"
done
