#!/bin/bash


#Automated Software Installer

echo "____________________________"
echo
echo "Automated Software Installer 🔥"
echo "____________________________"
echo
echo "Enter a list of tools"
read -a tools
echo

for i in ${tools[@]}
do
    sudo apt install $i -y
    echo
done
