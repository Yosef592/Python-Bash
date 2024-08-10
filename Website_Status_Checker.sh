#!/bin/bash


#Live_host_discovery

echo "___________________"
echo
echo "Live_Host_Discovery 🔥"
echo "___________________"
echo
echo "Enter a URL"
read -a url
echo
echo "Checking ..."
sleep 1s
echo


for i in ${url[@]}
do
	x=$(curl -o /dev/null -s -w "%{http_code}" "$i")
	if [[ $x == 200 || $x == 301 ]]
	then
		echo "$i  ==>  Host is UP !!! 👍   ( Status code: $x )"
	else
		echo "$i  ==>  Host is DOWN !!! 👎   ( Status code: $x )"
	fi
	echo
done
