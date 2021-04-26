#!/bin/bash
for ((i=$1;i<$2;i++))
do
mkdir IONION$i
cd IONION$i
cp ../resource/IONION_wat_svc.* .
cp ../resource/md_*.in .
cp ../resource/ION.slm .
sed -i s/XXX/$i/g ION.slm
sbatch ION.slm
cd ..
done
