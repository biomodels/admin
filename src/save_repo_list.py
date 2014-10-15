'''
Script to write a pickled list of current repos
'''

import pickle
from _repos import get_repos
from _constants import FILE_REPO_LIST

repos = get_repos()
repo_names = [repo.name for repo in repos]

pickle.dump(repo_names, open(FILE_REPO_LIST, 'w'))