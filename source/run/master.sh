#!/bin/bash
#for directory in Be Cu Ni Zn Co IONION Fe Mg V Mn Hg Cd IONION Sn Sr Ba
for ((j=0;j<20;j++))
do
cd IONION$j
### remove previous diff.out if it exists ###
if [[ -f diff.out ]]; then
rm diff.out
fi
cp ../resource/calc.in .
cp ../resource/process.sh .
sh process.sh
count=0;
total=0;
if [[ -f diff.out ]];then
for i in $( awk '{ print $1; }' diff.out )
do 
total=$(echo $total+$i | bc )
((count++))
done
echo "scale=5; $total / $count" | bc
fi
cd ..
done
