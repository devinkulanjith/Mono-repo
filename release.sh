#! /bin/bash

dir=$PWD

apps=$(<read_file.txt)

npm i node
npm i --global yarn
sudo yarn global add vtex
for name in $apps;
do
 cd $dir/$name
 echo "yes" | vtex release patch stable
done
