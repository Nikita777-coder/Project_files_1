#!/bin/bash
read -p "Введите два числа и операцию, которую хотите применить к ним" first_num second_num operand
if [[ ($operand ==  '/' || $operand == ':') && $second_num != 0 ]]; then
	res=$(($first_num/$second_num))
elif [[ $operand == '*' || $operand == 'x' || $operand == 'X' ]]
then
	res=$(($first_num*$second_num))
elif [[ $operand == '+' ]]
then
	res=$(($first_num+$second_num))
elif [[ $operand == '-' ]]
then
	res=$(($first_num-$second_num))
else
	echo "Division by zero"
fi
echo $res
