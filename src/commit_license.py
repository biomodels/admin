'''
Script to add the LICENSE file as a commit
'''

from _create import write_file, mkdirp
from _template import read_file
from _shell import shell
from _remove import remove
from _constants import FILE_REPO_LIST, DIR_REPOS, PATH_LICENSE_TEMPLATE
import pickle
import os

existing_repos = pickle.load(open(FILE_REPO_LIST, 'r'))

for id in existing_repos:
    if id == 'admin':
        continue
    print 'Working on %s' % id
    remove(DIR_REPOS)
    mkdirp(DIR_REPOS)
    shell(cmd='git clone git@github.com:biomodels/%s.git' % id, dir=DIR_REPOS)
    license_content = read_file(PATH_LICENSE_TEMPLATE)
    write_file('LICENSE.txt', id, license_content)
    shell(cmd='git add LICENSE.txt',
          dir=os.path.join(DIR_REPOS, id))
    shell(cmd=['git', 'commit', '-am', 'Added LICENSE'],
          dir=os.path.join(DIR_REPOS, id))
    shell(cmd=['git', 'push'],
          dir=os.path.join(DIR_REPOS, id))