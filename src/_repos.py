import json
import os
import urllib
from github import Github
import getpass

def get_repos():
    '''
    Returns a set of repo names
    '''
    user = raw_input('Github User: ')
    pw = getpass.getpass()
    g = Github(user, pw)
    
    org = g.get_organization('biomodels')
    
    return [repo for repo in org.get_repos()]