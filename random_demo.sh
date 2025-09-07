x=$(($RANDOM % 100))
y=$(($RANDOM % 100))
z=$(($RANDOM % 100))
echo $x $y $z

if [[ $x -gt $y && $x -gt $z ]]; then
    echo "x is the greatest"
elif [[ $y -gt $x && $y -gt $z ]]; then
    echo "y is the greatest"
else
    echo "z is the greatest"
fi