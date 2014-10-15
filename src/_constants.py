'''
Constants used by scripts and other modules
'''


def ab_path(path):
    '''
    Get absolute path for file
    '''
    import os
    return os.path.abspath(
                    os.path.join(
                        os.path.dirname(os.path.realpath(__file__)),
                        path
                    )
                )
                

VERSION = 20140916 # Version of BioModels used
DIR_REPOS = ab_path('../repos')
FILE_REPO_LIST = ab_path('../repos.pickle')
FILE_BLACKLIST = ab_path('../blacklist.pickle')
                
PATH_SETUP_TEMPLATE = ab_path('templates/setup.py.tpl')
PATH_MODEL_TEMPLATE = ab_path('templates/model.py.tpl')
PATH_INIT_TEMPLATE = ab_path('templates/__init__.py.tpl')
PATH_LICENSE_TEMPLATE = ab_path('templates/LICENSE.txt.tpl')
PATH_README_TEMPLATE = ab_path('templates/README.md.tpl')