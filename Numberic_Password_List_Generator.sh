#!/bin/bash



#Numberic_Password_List_Generator


intro()
{
	echo
	echo "_______________WELCOME TO P@CR7__________________"
	echo
	echo "~~~P@CR7 is generat a numberic password lists.~~~"
	echo "~~~~~start with 2 digits, end with 6 digits.~~~~~"
	echo "               DEVELOPED BY ^HXBNO^              "
	echo "_________________________________________________"
}


input()
{
	echo
	echo "Enter a digit (2 - 6)"
	read -p ">> " no
	echo
	echo
	echo "Please Wait..."
	echo
	echo
}


if_statment()
{
	if [[ $no == 2 ]]
	then
		for ((p=0; p<10; p++))
		do
			for ((a=0; a<10; a++))
			do
				echo $p$a >> Password_list_2.txt
			done
		done
		echo "SAVE TO 'Password_list_2.txt'"
		echo
	elif [[ $no == 3 ]]
	then
		for ((p=0; p<10; p++))
		do
			for ((a=0; a<10; a++))
			do
				for ((s=0; s<10; s++))
				do
					echo $p$a$s >> Password_list_3.txt
				done
			done
		done
		echo "SAVE TO 'Password_list_3.txt'"
		echo
	elif [[ $no == 4 ]]
	then
		for ((p=0; p<10; p++))
		do
			for ((a=0; a<10; a++))
			do
				for ((s=0; s<10; s++))
				do
					for ((w=0; w<10; w++))
					do
						echo $p$a$s$w >> Password_list_4.txt
					done
				done
			done
		done
		echo "SAVE TO 'Password_list_4.txt'"
		echo
	elif [[ $no == 5 ]]
	then
		for ((p=0; p<10; p++))
		do
			for ((a=0; a<10; a++))
			do
				for ((s=0; s<10; s++))
				do
					for ((w=0; w<10; w++))
					do
						for ((o=0; o<10; o++))
						do
							echo $p$a$s$w$o >> Password_list_5.txt
						done
					done
				done
			done
		done
		echo "SAVE TO 'Password_list_5.txt'"
		echo
	elif [[ $no == 6 ]]
	then
		for ((p=0; p<10; p++))
		do
			for ((a=0; a<10; a++))
			do
				for ((s=0; s<10; s++))
				do
					for ((w=0; w<10; w++))
					do
						for ((o=0; o<10; o++))
						do
							for ((r=0; r<10; r++))
							do
								echo $p$a$s$w$o$r >> Password_list_6.txt
							done
						done
					done
				done
			done
		done
		echo "SAVE TO 'Password_list_6.txt'"
		echo
	else
		echo "Always Enter (1 - 6)"
		echo "Try Again"
		echo
	fi
}


intro
input
if_statment