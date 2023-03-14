#!/bin/bash

git add -A
git status

read -p "Do you want to proceed? (y/n) " yn

case $yn in 
	[yY] ) echo ok, we will proceed;;
	[nN] ) echo exiting...;
        git reset
		exit;;
	* ) echo invalid response;
		exit;;
esac

read -p "Message: " msg
com_msg=""
if [ -z "$msg" ]; then
      com_msg="Working changes"
else
      com_msg=$msg"shoe"
fi
git commit -m "$com_msg"
git push