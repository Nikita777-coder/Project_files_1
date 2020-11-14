#!/bin/bash
all=/etc/passwd
echo "Создание пользователя"
read -p "Введите имя: " Name
grep $Name+":" $all >/dev/null
if [[ $? != 0 ]]; then
	read -p  "Введите пароль: " P
	read -p "Должен ли пользователь при первом заходе сменить пароль? " answer
	read -p "До какого дня аккаунт должен быть валиден?(YYYY-MM-DD) " day
	read -p "С какой периодичностью должен меняться пароль? " coun
	sudo useradd -e $day -p $P  $Name
	if [[ $answer == "yes" ]]; then
		sudo passwd -e $Name
	fi
	sudo chage -M $coun $Name
else
	echo "Имя занято"
fi 
