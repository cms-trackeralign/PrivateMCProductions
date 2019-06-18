#!/bin/bash

eval `scramv1 runtime -sh`
CMSSW_DIR=${CMSSW_BASE}/src/PrivateMCProductions/TkAlCosmics0T

if [ -d $CMSSW_DIR/outfiles ]; then
    echo "$CMSSW_DIR/outfiles already exists, skipping"
else
    mkdir $CMSSW_DIR/outfiles
fi

for i in {0..2000}; do   
    echo "------ submitting job with seed = $i"
    condor_submit par1=${i} par2=500000 par3=106X_mcRun3_2024_realistic_Candidate_2019_06_07_21_52_19 par4=2024 submit.sub par5=${CMSSW_DIR}
done

