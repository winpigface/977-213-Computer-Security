#!/bin/sh

#echo $FLAG > $(cat /dev/urandom | tr -cd 'a-f0-9' | head -c 32).txt
echo $(cat /dev/urandom | tr -cd 'a-f0-9' | head -c 32) > flag.txt
#unset FLAG
/etc/init.d/xinetd start;
sleep infinity;
