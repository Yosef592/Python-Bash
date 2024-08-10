#!/bin/bash


# Password Lists Generater

echo "___________________________"
echo
echo "Password Lists Generater 🔥"
echo "___________________________"
echo
read -p "Enter a length of a password list: >> " length
read -p "Enter a characters to includeing a password list: >> " characters
echo
touch Password_Lists.txt
echo "Generating ..."
for i in {1..50}
do
password=$(head /dev/urandom | tr -dc "$characters" | head -c "$length")
echo "$password" >> Password_Lists.txt
done
echo
echo "Password Lists is Successfully Generated, Save To 'Password_Lists.txt' "
echo
