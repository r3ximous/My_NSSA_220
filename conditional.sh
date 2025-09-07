#!/bin/bash
a=999
b=101

echo $a
echo $b

if [ $a > $b -a ! $a == $b ]
then
  echo "a is greater than b"
else
  echo "nah"
fi



