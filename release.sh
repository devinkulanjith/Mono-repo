#! /bin/bash

dir=$PWD

apps=$(<read_file.txt)

for name in $apps;
do
 cd $dir/$name
 echo "yes" | vtex release patch stable
done
