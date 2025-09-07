#!/bin/bash

# Initialize an array of size 100 to even numbers
i=0
until [ $i -eq 100 ]
do
    array[$i]=$((2 * i))
    i=$((i + 1))
done

# Print the array
echo "${array[@]}"