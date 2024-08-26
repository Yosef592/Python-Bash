#!/bin/bash       # This file is run in bash terminal.



# A Bash Script file extension is ".sh"

# To run a bash script file you can use this:
# 1, bash filename.sh
# 2, /bin/bash filename.sh
# 3, first give a excutable permision to the file and run a file:
#      - chmod +x filename.sh
#      - ./filename.sh



echo "kali linux"       # To display kali linux on the screen.
echo 'parrot sec'
echo                    # To display a new line

Name="josi"             # Create a var
number=97

echo $Name   			# Using a var
echo ${number}
echo "Hello $Name"
echo "Your number is ${number}"

set kali linux parrot ubuntu       # Create a values

echo $1 $3                         # Using a values by index number, index number is started with "1"

echo $HOME				# System Variable's
echo $USER
echo $RANDOM
echo $PWD
echo $SHELL

lists=("kali" "parrot" "ubuntu")     # Create a Arrays

echo ${lists[1]}                     # Using a Arrays by index number, index number is started with "0"
echo ${lists[@]}                     # "@" is all
echo ${!lists[@]}                    # "!" is index
echo ${#lists[@]}                    # "#" is index length

unset lists[2]                       # To delet "ubuntu" on the Array or index 2

read -p "Enter a name: " name           # Input
read -sp "Enter a password: " pass 		# To input a password or hide input
echo
read -a array   						# To input a list or arrays

echo $1 $2                              # Argument input

# This is comment

sleep 10s               # To keep out 10 second

echo $((10 + 5))        # operation

if [[ anme < ssdf ]]             # if, elif, else statment
then
echo "kali"
elif [[ sdf == sdfsd ]]
then
echo "parrot"
else
echo "ubuntu"
fi

for i in {1..100}                # for loop on range
do
echo $i
done

for i in $Var 					 # for loop in var
do
echo "somethink"
done

for ((i=0; i<10; i++))			 # for loop in no var, like a c or c++
do
echo "sdff"
done

x=0
while ((x < 10))                # while loop
do
echo $x
((x++))
done

while :							# infinity while loop
do
echo "hacking"
done

r=-1
while :
do
((r++))
if [[ $r == 10 ]]
then
break						# break statment
fi
done

function_name()				# Create a function
{
	function body
	function body
	function body
}

function_name    			# call a function




# Tip = 1, You can run a linux command inside bash script file
#       2, You can accsess a local file on "*"
#       3, You can accsess a bash terminal by "/bin/bash"
#       4, You can stop all bash script code by "exit 1"