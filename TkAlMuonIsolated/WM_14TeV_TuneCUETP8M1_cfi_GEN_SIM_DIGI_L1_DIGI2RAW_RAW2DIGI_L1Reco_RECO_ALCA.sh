#!/bin/bash

mySeed=$1
nEvts=$2
globalTag=$3
JobName=step1_WM_13TeV_TuneCUETP8M1_${nEvts}_evts_seed_$mySeed

echo  "Job started at " `date`

CMSSW_DIR=$4
LXBATCH_DIR=$PWD

cd ${CMSSW_BASE}/src
eval `scramv1 runtime -sh`
cd $LXBATCH_DIR

cp ${CMSSW_DIR}/WM_13TeV_TuneCUETP8M1_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_L1Reco_RECO_ALCA_Templ.py .
echo "cmsRun ${CMSSW_DIR}/WM_13TeV_TuneCUETP8M1_cfi_py_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_L1Reco_RECO_ALCA_Templ.py"

cmsRun WM_13TeV_TuneCUETP8M1_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_L1Reco_RECO_ALCA_Templ.py myseed=${mySeed} maxEvents=${nEvts} GlobalTag=${globalTag} >& ${JobName}.out

echo "Content of working directory is: " `ls -lrt`

eos mkdir -p /eos/cms/store/group/alca_trackeralign/$USER/test_out/WMuNuRun3MCProduction/

for payloadOutput in $(ls *root ); do xrdcp -f $payloadOutput root://eoscms.cern.ch//eos/cms/store/group/alca_trackeralign/$USER/test_out/WMuNuRun3MCProduction/step1_ZMM_13TeV_TuneCUETP8M1_${globalTag}_${nEvts}_evts_seed_${mySeed}.root ; done

echo  "Job ended at " `date`

exit 0
