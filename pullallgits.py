## pulls all updates from the students repos in the file DSPS2021.csv"
## run as
#####$ python pullallgits.py Tue
## or
#####$ python pullallgits.py Thu
##
##must have env variable DSPS2021 set up and pointing to a
import os
import sys
import glob


### checking env variable is set up
dspsdir = os.getenv("DSPS2021")
if dspsdir is None:
	print ("make sure the env variable DSPS2019 is set up")
	sys.exit()

dspsdir = dspsdir + "STUDREPOS"

### moving to work into dspsdir
os.chdir(dspsdir)
print (dspsdir)
cwd = os.getcwd()
print (" you are in %s"%cwd)

### checking you are in the right repo
if not (cwd + '/').replace('//', '/') == (dspsdir + '/' + 'STUDREPOS' + "/").replace('//', '/'):
        print ("something is wrong:I cannot go to the DSPS2019 directory")

allrepos = glob.glob("*")

for repo in allrepos:
        os.chdir(dspsdir + "/"  + "/" + repo)
        os.system("git pull")
        os.chdir(dspsdir + "/" )
        

