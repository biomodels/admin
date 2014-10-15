'''
Script to create initial repositories for all biomodels
'''

from _create import create
from _remove import remove
from _shell import shell
from _constants import VERSION, DIR_REPOS, FILE_REPO_LIST, FILE_BLACKLIST
import os
import pickle
import bioservices


s = bioservices.BioModels()

ids = s.getAllModelsId() 
# ids = ['BIOMD0000000051']
# all = s.getAllModelsId()
# curated = s.getAllCuratedModelsId()
# noncurated = s.getAllNonCuratedModelsId()

existing_repos = set(pickle.load(open(FILE_REPO_LIST, 'r')))
blacklist = set(pickle.load(open(FILE_BLACKLIST, 'r')))

# list of ids not found in union of the two sets
id_list = [id for id in ids if id not in existing_repos | blacklist] 

for id in id_list:
    print 'Creating %s' % id
    remove(DIR_REPOS)
    create(id, DIR_REPOS, VERSION)
    shell(cmd='hub create biomodels/%s' % id, dir=os.path.join(DIR_REPOS, id))
    shell(cmd='git init', dir=os.path.join(DIR_REPOS, id))
    shell(cmd='git add .', dir=os.path.join(DIR_REPOS, id))
    shell(cmd=['git', 'commit', '-m', 'Initial Commit'], dir=os.path.join(DIR_REPOS, id))
    shell(cmd='git remote add origin git@github.com:biomodels/%s.git' % id, dir=os.path.join(DIR_REPOS, id))
    shell(cmd='git push -u origin master', dir=os.path.join(DIR_REPOS, id))
    shell(cmd='git tag %s' % VERSION, dir=os.path.join(DIR_REPOS, id))
    shell(cmd='git push --tags', dir=os.path.join(DIR_REPOS, id))