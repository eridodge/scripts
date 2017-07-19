#!/bin/bash

########################################################
#Made in Cooperation by Eric Dodge & Mitchell Pemberton#
#				   Created 07/13/2017				   #
########################################################

#Asks which directory or file they want to hash
#echo "Which directory/file would you like to hash? (Full File Path)";
#read path

#Asks which kind of hash the user wants
echo "Which type of hash would you like? (md5, sha256, sha512)";
read answer

cd "$path"

if [ "$answer" == "md5" ]; then
#Gets the MD5 hash and the dates modified of the directory 
	 xdg-open $path
	
	find -L -type f -printf '%Tc %p\n' -exec md5sum "{}" \; >> md5sum.md5


	md5sum -c md5sum.md5 >> checklog.md5


	chmod 0444 md5sum.md5

fi

if [ "$answer" == "sha256" ]; then
#Gets the sha256 hash and the dates modified of the directory 
	xdg-open $path	

	find -L -type f -printf '%Tc %p\n' -exec sha256sum "{}" \; >> sha256sum.sha256


	sha256sum -c sha256sum.sha256 >> checklog.sha256


	chmod 0444 sha256sum.sha256

fi

if [ "$answer" == "sha512" ]; then
#Gets the sha512 hash and the dates modified of the directory 
	xdg-open $path	

	find -L -type f -printf '%Tc %p\n' -exec sha512sum "{}" \; >> sha512sum.sha512


	sha512sum -c sha512sum.sha512 >> checklog.sha512


	chmod 0444 sha512sum.sha512
	
fi
