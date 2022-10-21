#! /bin/bash

dir=$PWD

apps=$(<read_file.txt)

for name in $apps;
do
 cd $dir/$name
 gnome-terminal --wait -- vtex release pre stable
done
