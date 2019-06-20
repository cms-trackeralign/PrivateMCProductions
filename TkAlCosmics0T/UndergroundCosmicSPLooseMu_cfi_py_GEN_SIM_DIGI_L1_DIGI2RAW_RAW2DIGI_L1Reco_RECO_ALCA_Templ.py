# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: UndergroundCosmicSPLooseMu_cfi.py --conditions auto:phase1_2018_cosmics -s GEN,SIM,DIGI:pdigi_valid,L1,DIGI2RAW,RAW2DIGI,L1Reco,RECO,ALCA:TkAlCosmics0T -n 10 --era Run2_2018 --eventcontent ALCARECO --scenario cosmics --datatier ALCARECO --beamspot Realistic25ns13TeVEarly2018Collision --no_exec
import FWCore.ParameterSet.Config as cms
import FWCore.ParameterSet.VarParsing as VarParsing

from Configuration.Eras.Era_Run3_cff import Run3
process = cms.Process('RECO',Run3)


###################################################################
# Setup 'standard' options
###################################################################
options = VarParsing.VarParsing()

options.register('myseed',
                 1,
                 VarParsing.VarParsing.multiplicity.singleton,
                 VarParsing.VarParsing.varType.int,
                 "my seed for the job (1 is default)")

options.register('maxEvents',
		 -1,
		 VarParsing.VarParsing.multiplicity.singleton,
		 VarParsing.VarParsing.varType.int,
		 "Number of events to process (-1 for all)")

options.register ('GlobalTag',
                  '106X_mcRun3_2023_realistic_Candidate_2019_06_07_21_52_54',
                  VarParsing.VarParsing.multiplicity.singleton, # singleton or list
                  VarParsing.VarParsing.varType.string,          # string, int, or float
		  "Global Tag to select")

options.parseArguments()

print "my seed is: ", options.myseed

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.MessageLogger.destinations = ['cout', 'cerr']
process.MessageLogger.cerr.FwkReport.reportEvery = 10000

process.load('Configuration.EventContent.EventContentCosmics_cff')
process.load('SimGeneral.MixingModule.mixCosmics_cfi')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.Geometry.GeometrySimDB_cff')
process.load('Configuration.StandardSequences.MagneticField_cff')
process.load('Configuration.StandardSequences.Generator_cff')
process.load('Configuration.StandardSequences.VtxSmearedNoSmear_cff')
process.load('GeneratorInterface.Core.genFilterSummary_cff')
process.load('Configuration.StandardSequences.SimNOBEAM_cff')
process.load('Configuration.StandardSequences.DigiCosmics_cff')
process.load('Configuration.StandardSequences.SimL1Emulator_cff')
process.load('Configuration.StandardSequences.DigiToRaw_cff')
process.load('Configuration.StandardSequences.RawToDigi_cff')
process.load('Configuration.StandardSequences.L1Reco_cff')
process.load('Configuration.StandardSequences.ReconstructionCosmics_cff')
process.load('Configuration.StandardSequences.AlCaRecoStreamsMC_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

# configure seed
process.RandomNumberGeneratorService.generator.initialSeed = cms.untracked.uint32(options.myseed)
process.RandomNumberGeneratorService.generator.engineName = cms.untracked.string('TRandom3')

process.RandomNumberGeneratorService.VtxSmeared.initialSeed = cms.untracked.uint32(options.myseed)
process.RandomNumberGeneratorService.VtxSmeared.engineName = cms.untracked.string('TRandom3') 

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(options.maxEvents)
)

myFirstEvent = (options.maxEvents * options.myseed)+1
print "firs Event:",myFirstEvent

# Input source
process.source = cms.Source("EmptySource",
			    firstEvent = cms.untracked.uint32(myFirstEvent),
			    firstLuminosityBlock = cms.untracked.uint32(options.myseed+1)
			    )

process.options = cms.untracked.PSet()

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    annotation = cms.untracked.string('UndergroundCosmicSPLooseMu_cfi.py nevts:10'),
    name = cms.untracked.string('Applications'),
    version = cms.untracked.string('$Revision: 1.19 $')
)

from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag,options.GlobalTag, '')

process.GlobalTag.toGet = cms.VPSet(
     cms.PSet(record = cms.string('BeamSpotObjectsRcd'),
          tag = cms.string('BeamSpotObjects_Realistic25ns_13TeVCollisions_RoundOpticsLowSigmaZ_RunBased_v1_mc'),
          connect = cms.string("frontier://FrontierProd/CMS_CONDITIONS"),
          ),    
           cms.PSet(record = cms.string('SiPixelDynamicInefficiencyRcd'),
          tag = cms.string('SiPixelDynamicInefficiency_PhaseI_Run3Studies_v2'),
         connect = cms.string("frontier://FrontierProd/CMS_CONDITIONS"),
          ),    
    cms.PSet(record = cms.string('SiPixelQualityFromDbRcd'),
         label = cms.untracked.string('forDigitizer'),
          tag = cms.string('SiPixelQuality_forDigitizer_phase1_Run3Endof3years'),
         connect = cms.string("frontier://FrontierProd/CMS_CONDITIONS"),
         ),    
     )


# Output definition
outrootfile='file:step1_UndergroundCosmicSPLooseMu_'+str(process.GlobalTag.globaltag.value())+"_"+str(options.maxEvents)+'_evts_seed_'+str(options.myseed)+'.root'
print 'output file name:', outrootfile

# Additional output definition
process.ALCARECOStreamTkAlCosmics0T = cms.OutputModule("PoolOutputModule",
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring(
            'pathALCARECOTkAlCosmicsCTF0T', 
            'pathALCARECOTkAlCosmicsCosmicTF0T', 
            'pathALCARECOTkAlCosmicsRegional0T'
        )
    ),
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('ALCARECO'),
        filterName = cms.untracked.string('TkAlCosmics0T')
    ),
    eventAutoFlushCompressedSize = cms.untracked.int32(5242880),
    fileName = cms.untracked.string(outrootfile),
    outputCommands = cms.untracked.vstring(
        'drop *', 
        'keep *_ALCARECOTkAlCosmicsCTF0T_*_*', 
        'keep *_ALCARECOTkAlCosmicsCosmicTF0T_*_*', 
        'keep *_ALCARECOTkAlCosmicsRegional0T_*_*', 
        'keep siStripDigis_DetIdCollection_*_*', 
        'keep L1AcceptBunchCrossings_*_*_*', 
        'keep L1GlobalTriggerReadoutRecord_gtDigis_*_*', 
        'keep *_TriggerResults_*_*', 
        'keep DcsStatuss_scalersRawToDigi_*_*', 
        'keep SiPixelCluster*_siPixelClusters_*_*', 
        'keep SiStripCluster*_siStripClusters_*_*', 
        'keep recoMuons_muons1Leg_*_*'
    )
)

# Other statements
process.genstepfilter.triggerConditions=cms.vstring("generation_step")
process.mix.digitizers = cms.PSet(process.theDigitizersValid)
process.ALCARECOEventContent.outputCommands.extend(process.OutALCARECOTkAlCosmics0T_noDrop.outputCommands)

process.cosmicInTracker = cms.EDFilter("CosmicGenFilterHelix",
    charges = cms.vint32(1, -1),
    doMonitor = cms.untracked.bool(False),
    maxZ = cms.double(212.0),
    minP = cms.double(0.0),
    minPt = cms.double(0.0),
    minZ = cms.double(-212.0),
    pdgIds = cms.vint32(-13, 13),
    propagator = cms.string('SteppingHelixPropagatorAlong'),
    radius = cms.double(80.0),
    src = cms.InputTag("generator","unsmeared")
)


process.cosmicInPixelLoose = cms.EDFilter("CosmicGenFilterHelix",
    charges = cms.vint32(1, -1),
    doMonitor = cms.untracked.bool(False),
    maxZ = cms.double(100.0),
    minP = cms.double(0.0),
    minPt = cms.double(0.0),
    minZ = cms.double(-100.0),
    pdgIds = cms.vint32(-13, 13),
    propagator = cms.string('SteppingHelixPropagatorAlong'),
    radius = cms.double(20.0),
    src = cms.InputTag("generator","unsmeared")
)


process.generator = cms.EDProducer("CosMuoGenProducer",
    AcptAllMu = cms.bool(False),
    ClayWidth = cms.double(50000.0),
    ElossScaleFactor = cms.double(1.0),
    MTCCHalf = cms.bool(False),
    MaxEnu = cms.double(10000.0),
    MaxP = cms.double(3000.0),
    MaxPhi = cms.double(360.0),
    MaxT0 = cms.double(12.5),
    MaxTheta = cms.double(84.0),
    MinEnu = cms.double(10.0),
    MinP = cms.double(10.0),
    MinP_CMS = cms.double(-1.0),
    MinPhi = cms.double(0.0),
    MinT0 = cms.double(-12.5),
    MinTheta = cms.double(0.0),
    MultiMuon = cms.bool(False),
    MultiMuonFileFirstEvent = cms.int32(1),
    MultiMuonFileName = cms.string('CORSIKAmultiMuon.root'),
    MultiMuonNmin = cms.int32(2),
    NuProdAlt = cms.double(7500000.0),
    PlugVx = cms.double(0.0),
    PlugVz = cms.double(-14000.0),
    RadiusOfTarget = cms.double(8000.0),
    RhoAir = cms.double(0.001214),
    RhoClay = cms.double(2.3),
    RhoPlug = cms.double(2.5),
    RhoRock = cms.double(2.5),
    RhoWall = cms.double(2.5),
    TIFOnly_constant = cms.bool(False),
    TIFOnly_linear = cms.bool(False),
    TrackerOnly = cms.bool(False),
    Verbosity = cms.bool(False),
    ZCentrOfTarget = cms.double(0.0),
    ZDistOfTarget = cms.double(15000.0)
)


process.SteppingHelixPropagatorAlong = cms.ESProducer("SteppingHelixPropagatorESProducer",
    ApplyRadX0Correction = cms.bool(True),
    AssumeNoMaterial = cms.bool(False),
    ComponentName = cms.string('SteppingHelixPropagatorAlong'),
    NoErrorPropagation = cms.bool(False),
    PropagationDirection = cms.string('alongMomentum'),
    SetVBFPointer = cms.bool(False),
    VBFName = cms.string('VolumeBasedMagneticField'),
    debug = cms.bool(False),
    endcapShiftInZNeg = cms.double(0.0),
    endcapShiftInZPos = cms.double(0.0),
    returnTangentPlane = cms.bool(True),
    sendLogWarning = cms.bool(False),
    useEndcapShiftsInZ = cms.bool(False),
    useInTeslaFromMagField = cms.bool(False),
    useIsYokeFlag = cms.bool(True),
    useMagVolumes = cms.bool(True),
    useMatVolumes = cms.bool(True),
    useTuningForL2Speed = cms.bool(False)
)


process.ProductionFilterSequence = cms.Sequence(process.generator+process.cosmicInPixelLoose)

# Path and EndPath definitions
process.generation_step = cms.Path(process.pgen)
process.simulation_step = cms.Path(process.psim)
process.digitisation_step = cms.Path(process.pdigi_valid)
process.L1simulation_step = cms.Path(process.SimL1Emulator)
process.digi2raw_step = cms.Path(process.DigiToRaw)
process.raw2digi_step = cms.Path(process.RawToDigi)
process.L1Reco_step = cms.Path(process.L1Reco)
process.reconstruction_step = cms.Path(process.reconstructionCosmics)
process.genfiltersummary_step = cms.EndPath(process.genFilterSummary)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.ALCARECOStreamTkAlCosmics0TOutPath = cms.EndPath(process.ALCARECOStreamTkAlCosmics0T)

# Schedule definition
process.schedule = cms.Schedule(process.generation_step,process.genfiltersummary_step,process.simulation_step,process.digitisation_step,process.L1simulation_step,process.digi2raw_step,process.raw2digi_step,process.L1Reco_step,process.reconstruction_step,process.pathALCARECOTkAlCosmicsCTF0T,process.pathALCARECOTkAlCosmicsCosmicTF0T,process.pathALCARECOTkAlCosmicsRegional0T,process.endjob_step,process.ALCARECOStreamTkAlCosmics0TOutPath)
from PhysicsTools.PatAlgos.tools.helpers import associatePatAlgosToolsTask
associatePatAlgosToolsTask(process)
# filter all path with the production filter sequence
for path in process.paths:
	getattr(process,path)._seq = process.ProductionFilterSequence * getattr(process,path)._seq 


# Customisation from command line

#Have logErrorHarvester wait for the same EDProducers to finish as those providing data for the OutputModule
from FWCore.Modules.logErrorHarvester_cff import customiseLogErrorHarvesterUsingOutputCommands
process = customiseLogErrorHarvesterUsingOutputCommands(process)

# Add early deletion of temporary data products to reduce peak memory need
from Configuration.StandardSequences.earlyDeleteSettings_cff import customiseEarlyDelete
process = customiseEarlyDelete(process)
# End adding early deletion
