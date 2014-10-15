'''
Functions for removing folders and files
'''

import shutil
import os

def remove(path):
    if os.path.exists(path):
        shutil.rmtree(path)
    else:
        print '%s does not exist so did not remove.' % path