import os
eventsToSubmit = 10000
Njobs =250 
InitialSeed = 1
globalTag = "106X_mcRun3_2023_realistic_Candidate_2019_06_19_15_56_48"
cmssw_base = os.environ['CMSSW_BASE']
cmssw_base+= "/src/PrivateMCProductions/TkAlMuonIsolated"

submitFile = open("job2023.submit", "w")

arg_string="" 
for i in range(InitialSeed, Njobs+InitialSeed):
    arg_string+="%i %i %s 2023 %s\n"%(i,eventsToSubmit,globalTag,cmssw_base)

content = "universe = vanilla\n"
content += "executable = WM_13TeV_TuneCUETP8M1cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_L1Reco_RECO_ALCA_Templ.sh\n"
content += "output                = %s/outfiles/step1_WM_13TeV_TuneCUETP8M1_%s_evts_$(ClusterId).$(ProcId).out\n"%(cmssw_base,str(eventsToSubmit))
content += "error                 = %s/outfiles/step1_WM_13TeV_TuneCUETP8M1_%s_evts_$(ClusterId).$(ProcId).err\n"%(cmssw_base,str(eventsToSubmit))
content += "log                   = %s/outfiles/step1_WM_13TeV_TuneCUETP8M1_%s_evts_$(ClusterId).$(ProcId).log\n"%(cmssw_base,str(eventsToSubmit))
content += "transfer_output_files = \"\" \n"
content += "+JobFlavour = 'workday'  \n"
content += "Queue Arguments from (\n"
content += "%s" %arg_string
content += ")"

submitFile.write(content)
submitFile.close()

os.system("condor_submit job2023.submit")
