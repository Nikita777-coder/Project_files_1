#!/bin/bash
read  -p "Введите Сиситему Исчисления и число в СИ: "  SI data
if [[ $SI == "days" ]]; then
	date -d @$(( $data*24*60*60 ))
elif [[ $SI == "years" ]] 
then
	date -d @$(( $data*365*24*60*60 ))
elif [[ $SI == "hours" ]] 
then
	date -d @$(( $data*60*60 ))
elif [[ $SI == "minutes" ]]
then 
	date -d @$(( $data*60 ))
elif [[ $SI == "seconds" ]] 
then 
	date -d @$(( $data ))
else
	echo "Ваша СИ выходит за пределы задуманной: [seconds;years]"
fi

