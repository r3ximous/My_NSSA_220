#!/bin/bash

# Read integer N from user
echo "How many integers:" 
read N

#for loop for the sum of 1^2 + 2^2 + 3^2 + ... + N^2
for ((i=1 ; i<=N ; i++))
do
    sum=$((sum + i*i))
done

#while loop for the sum of 1^2 + 2^2 + 3^2 + ... + N^2
sum2=0
i=1
while [ $i -le $N ]
do
    sum2=$((sum2 + i*i))
    i=$((i + 1))
done

# Print the sum
echo "The sum of the squares of the first $N integers is: 
$sum and $sum2"

#until loop for the sum of 1^2 + 2^2 + 3^2 + ... + N^2
sum3=0
i=1
until [ $i -gt $N ]
do
    sum3=$((sum3 + i*i))
    i=$((i + 1))
done