#! /bin/bash

dir=$PWD

apps=$(<read_file.txt)


vtex use testautomation

for name in $apps;
do
 cd $dir/$name
 echo "yes" | vtex publish --force
 sleep 5
 echo "yes" | vtex install
 sleep 5

done
