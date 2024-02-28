#!/bin/bash

for ip in $(cat ips.txt); do
    ping -c 1 $ip &
done
