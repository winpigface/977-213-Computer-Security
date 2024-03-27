#!/bin/sh

echo $(cat /dev/urandom | tr -cd 'a-f0-9' | head -c 32) > flagQ1.txt
echo $(cat /dev/urandom | tr -cd 'a-f0-9' | head -c 32) > flagQ2.txt
echo $(cat /dev/urandom | tr -cd 'a-f0-9' | head -c 32) > flagQ3.txt
echo $(cat /dev/urandom | tr -cd 'a-f0-9' | head -c 32) > flagQ4.txt
echo $(cat /dev/urandom | tr -cd 'a-f0-9' | head -c 32) > flagQ5.txt
#unset FLAG
/etc/init.d/xinetd start;
sleep infinity;
