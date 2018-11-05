#!/bin/sh

#check the homebridge run status
status=`/etc/init.d/homebridge status`
echo $status
if [ "$status" = "Stopped" ] 
then
	`/etc/init.d/homebridge start>/dev/null 2>&1`
	echo "Starting homebridge now"
else 
	echo "The homebridge is "$status
fi
