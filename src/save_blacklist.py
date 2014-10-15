'''
Create blacklisted models that were not created
'''

from _constants import FILE_BLACKLIST
import pickle

blacklist = [
    'MODEL1311110001',
    'MODEL3883569319',
    'MODEL1402200000'
]

pickle.dump(blacklist, open(FILE_BLACKLIST, 'w'))