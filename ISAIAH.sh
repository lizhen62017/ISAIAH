#!/bin/bash

# Initiation, remember loadamber
input="input.in"
wnm=(2000 4000 6000 8000)
sze=(17 23 27 29)

# Read values from input.in
while IFS= read -r line
do
  wat=$(echo $line | awk '{ print $1 }')
  ion=$(echo $line | awk '{ print $2 }')
  chg=$(echo $line | awk '{ print $3 }')
  par=$(echo $line | awk '{ print $4 }')
  num=$(echo $line | awk '{ print $5 }')
  mas=$(echo $line | awk '{ print $6 }')
  rmn=$(echo $line | awk '{ print $7 }')
  eps=$(echo $line | awk '{ print $8 }')
  c4v=$(echo $line | awk '{ print $9 }')

  # Construct files and fire MDs
  if [[ ! -d ${wat}_${ion} ]]
  then 
    mkdir ${wat}_${ion}
  fi
  mkdir ${wat}_${ion}/structgen_${par}
  mkdir ${wat}_${ion}/run_${par}
  for ((i=0;i<4;i++))
  do
    cp -r source/structgen ${wat}_${ion}/structgen_${par}/${wnm[${i}]}WAT
    cd ${wat}_${ion}/structgen_${par}/${wnm[${i}]}WAT
    if [[ ${wat} == 'fb3' ]]
    then
      sed -i "s/WATWAT/tip3pfb/g" leap.in
    elif [[ ${wat} == 'fb4' ]]
    then
      sed -i "s/WATWAT/tip4pfb/g" leap.in
    else
      sed -i "s/WATWAT/${wat}/g" leap.in
    fi
    sed -i "s/WATCAP/${wat^^}/g; s/IONION/${ion}/g; s/IONCAP/${ion^^}/g; s/CHGCHG/${chg}/g; s/CHGNUM/${chg:0:1}/g; s/NUMNUM/${num}/g; s/MASMAS/${mas}/g; s/RMNRMN/${rmn}/g; s/EPSEPS/${eps}/g; s/C4VC4V/${c4v}/g; s/SZESZE/${sze[${i}]}/g" *
    tleap -s -f leap.in
    if [[ ${par} == '1264' ]]
    then
      parmed -i dflt_1264
    else
      mv ${ion}_wat.prmtop ${ion}_wat_svc.prmtop
      mv ${ion}_wat.inpcrd ${ion}_wat_svc.inpcrd
    fi
    cd ../../..
    cp -r source/run ${wat}_${ion}/run_${par}/${wnm[${i}]}WAT
    cd ${wat}_${ion}/run_${par}/${wnm[${i}]}WAT
    sed -i "s/IONION/${ion}/g" *.sh
    cp ../../structgen_${par}/${wnm[${i}]}WAT/${ion}_wat_svc.* resource/
    sed -i "s/IONION/${ion}/g; s/PARPAR/${par}/g; s/WNMWNM/${wnm[${i}]:0:1}/g" resource/*
    if [[ ${par} == '1264' ]]
    then
      sed -i "s/lj1264=0/lj1264=1/g" resource/*
    fi
    sh submit.sh 0 20
    cd ../../..
  done
done < "$input"
