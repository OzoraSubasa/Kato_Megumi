#!/system/bin/sh

echo "start statistic"
CPUFILE=cpu.txt
MEMFILE=mem.txt
SWAPFILE=swap.txt
SleepInterval=900

if [ -e $CPUFILE ]
then
	echo $CPUFILE "exist, and will be removed."
	rm $CPUFILE
fi

if [ -e $MEMFILE ]
then
	echo $MEMFILE "exist, and will be removed."
	rm $MEMFILE
fi

if [ -e $SWAPFILE ]
then
	echo $SWAPFILE "exist, and will be removed."
	rm $SWAPFILE
fi

while :
do
	cpu=`top -n 1 | grep cpu`
	echo $cpu>>$CPUFILE
    mem=`top -n 1 | grep Mem`
	echo $mem>>$MEMFILE
	swap=`top -n 1 | grep Swap`
	echo $swap>>$SWAPFILE
	sleep $SleepInterval
done
