# PrivateMCProductions: TkAlZMuMu

```
cmsrel CMSSW_10_6_0_patch1
cd CMSSW_10_6_0_patch1/src
git clone -b run3prod git@github.com:cms-trackeralign/PrivateMCProductions.git
cd PrivateMCProductions/TkAlZMuMu/
mkdir outfiles
./submitAllSeeds.sh
```

this will create 2.5M events (250 jobs for 10k Z->mu,mu events each). N.B. efficiency is not 100%, so you'll see many less reconstruction-level events.
