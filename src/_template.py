'''
Functions for templating of repo content files
'''

from jinja2 import Template
import _constants as c

def read_file(path):
    with open(path,'r') as f:
        output = f.read()
    return output
    
def render_template(file_path, params):
    s = read_file(file_path)
    template = Template(s)
    return template.render(params)
    
def setuppy_template(params):
    s = read_file(c.PATH_SETUP_TEMPLATE)
    template = Template(s)
    return template.render(params)
    
def modelpy_template(params):
    s = read_file(c.PATH_MODEL_TEMPLATE)
    template = Template(s)
    return template.render(params)

def initpy_template(params):
    s = read_file(c.PATH_INIT_TEMPLATE)
    template = Template(s)
    return template.render(params)