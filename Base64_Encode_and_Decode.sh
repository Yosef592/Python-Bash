#!/bin/bash


# base64 encode and decode

echo "________________________"
echo
echo "Base64 Encode and Decode 🔥"
echo "________________________"
echo
read -p "Encode or Decode (e,d): >> " base64
if [[ $base64 == "e" ]]
then
echo
read -p "Enter a Word To Encode: >> " Eword
E=$(echo "$Eword" | base64)
echo
echo "$Eword  <==>  $E"
echo
elif [[ $base64 == "d" ]]
then
echo
read -p "Enter a Word To Decode: >> " Dword
D=$(echo "$Dword" | base64 -d)
echo
echo "$Dword  <==>  $D"
echo
else
echo
echo "ERROR"
echo
fi
