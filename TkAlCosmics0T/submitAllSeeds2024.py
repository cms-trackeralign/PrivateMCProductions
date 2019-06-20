import os
eventsToSubmit = 500000
Njobs =2000 
InitialSeed = 1
globalTag = "106X_mcRun3_2024_realistic_Candidate_2019_06_07_21_52_19"
cmssw_base = os.environ['CMSSW_BASE']
cmssw_base+= "/src/PrivateMCProductions/TkAlCosmics0T"

submitFile = open("job2024.submit", "w")

arg_string="" 
for i in range(InitialSeed, Njobs+InitialSeed):
    arg_string+="%i %i %s 2024 %s\n"%(i,eventsToSubmit,globalTag,cmssw_base)

content = "universe = vanilla\n"
content += "executable = UndergroundCosmicSPLooseMu_cfi_py_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_L1Reco_RECO_ALCA_Templ.sh\n"
content += "output                = %s/outfiles/step1_UndergroundCosmicSPLooseMu_%s_evts_$(ClusterId).$(ProcId).out\n"%(cmssw_base,str(eventsToSubmit))
content += "error                 = %s/outfiles/step1_UndergroundCosmicSPLooseMu_%s_evts_$(ClusterId).$(ProcId).err\n"%(cmssw_base,str(eventsToSubmit))
content += "log                   = %s/outfiles/step1_UndergroundCosmicSPLooseMu_%s_evts_$(ClusterId).$(ProcId).log\n"%(cmssw_base,str(eventsToSubmit))
content += "transfer_output_files = \"\" \n"
content += "+JobFlavour = 'workday'  \n"
content += "Queue Arguments from (\n"
content += "%s" %arg_string
content += ")"

submitFile.write(content)
submitFile.close()

os.system("condor_submit job2024.submit")
