'''
Functions for operating running shell commands
'''

from subprocess import Popen, PIPE
import os
from six import string_types


def shell(cmd='', dir=os.getcwd()):
    '''
    Execute shell commands in the directory
    '''
    if isinstance(cmd, string_types):
        cmd = cmd.split(' ')
    process = Popen(cmd, stdout=PIPE, stderr=PIPE, cwd=dir)
    stdout, stderr = process.communicate()
    if stderr or stdout:
        print '------------------------------'
    if stdout:
        print 'STDOUT: %s' % stdout
    if stderr:
        print 'STDERR: %s' % stderr
    
    return stdout, stderr
    