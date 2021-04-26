#!/bin/bash
for ((i=0;i<80;i++))
do
if [[ -f md_diff_$i.netcdf ]];then
cpptraj IONION_wat_svc.prmtop < calc.in > out
awk '/IONION_dc_AvgDr/{print $2}' IONION_dc.dat >> diff.out
j=`echo $i+1|bc`
sed -i "s/md_diff_$i/md_diff_$j/g" calc.in
else
echo failedatcycle $i
exit
fi
#cat calc.in
done
