#!/bin/bash
i=0
echo "from $i"
until [ $i -gt 10 ]
do
    echo "$i"
    i=$((i+1))
done

