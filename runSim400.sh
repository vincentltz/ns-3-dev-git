
FILES=~/randomTopolog/Net_400_*

for f in $FILES
do

	echo $f
	#./waf
	./waf --run "topoTestAdhoc --infile="$f" --outHopsFile=scratch/maxhopscmd_400.txt --outTimeFile=scratch/maxtimecmd_400.txt --outAvgMsgFile=scratch/avgmsgcmd_400.txt"
done
