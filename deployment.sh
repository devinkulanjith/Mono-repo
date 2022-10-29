#! /bin/bash

dir=$PWD

apps=$(<read_file.txt)


for name in $apps;
do
 cd $dir/$name
 echo "yes" | vtex publish --force
 sleep 5

 echo "yes" | vtex install

done
