#!/bin/bash

# Read three integers from the user
echo "Enter first integer:"
read a
echo "Enter second integer:"
read b
echo "Enter third integer:"
read c

# Calculate the sum
sum=$((a + b + c))

# Print the sum
echo "The sum of the three integers is: $sum"