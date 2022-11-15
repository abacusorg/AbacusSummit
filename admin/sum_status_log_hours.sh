#!/usr/bin/env bash

# Sum the hours for each sim arg, using status.log

running=0
for sim in "$@"; do
    tot=$(\grep -Po 'after.*hours' $sim/status.log | awk '{sum+=$2} END {print sum}')
    if [ -z "$tot" ]; then
        continue
    fi
    echo "$sim: $tot"
    running=$(echo "${running} + ${tot}" | bc)
done
echo -e "\nTotal: ${running}"
