## clones all the students repos in the file DSPS2021.csv"
## run as
#####$ python gitallrepos.py Tue
## or
#####$ python gitallrepos.py Thu
##
##must have env variable DSPS2021 set up and pointing to a
import pandas as pd
import os
import sys

if len(sys.argv) == 1:
        filename = "DSPSstudents.csv"
else:
        filename = sys.argv[1]
### read in file
tmp = pd.read_csv(filename)[['GitHub DSPS Repo', 'Student']]
tmp.dropna(inplace=True)
#tmp['GitHub Link'] = tmp['GitHub handle'].apply(lambda x:'https://github.com/' + x)

tmp.rename({'GitHub DSPS Repo':'GitHub Link'}, axis=1, inplace=True)

### checking env variable is set up
dspsdir = os.getenv("DSPS2019")
if dspsdir is None:
	print ("make sure the env variable DSPS is set up")
	sys.exit()

### creating puidir if needed
if not os.path.isdir(dspsdir):
        os.system("mkdir -p %s"%dspsdir)
        #print ("make sure %s exists and is a directory"%dspsdir)
	#sys.exit()

### moving to work into dspsdir
os.chdir(dspsdir)
print (dspsdir)
cwd = os.getcwd()
print (" you are in %s"%cwd)

### checking you are in the right repo
if not (cwd + '/').replace('//', '/') == (dspsdir + '/').replace('//', '/') and not (cwd + '/').replace('//', '/').replace('gpfs1','home') == (dspsdir + '/').replace('//', '/'):

        print ("something is wrong:I cannot go to the DSPS directory")

### creating subdir for students session and moving to work in there
if not os.path.isdir(dspsdir + '/' + "STUDREPOS"):
        os.system("mkdir STUDREPOS")
os.chdir(dspsdir + '/' + "STUDREPOS")

## prining the repo names and cloning
for i,n in enumerate(tmp['Student'].values):
        print (tmp['GitHub Link'].values[i])

for i,n in enumerate(tmp['Student'].values):
        os.system ("git clone " + tmp['GitHub Link'].values[i])#+"/PUI2018_"+n)

