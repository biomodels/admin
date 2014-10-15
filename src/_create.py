'''
Functions for creating repo contents for a biomodel
'''
import sys
import os
import html2text
h = html2text.HTML2Text()

def mkdirp(path):
    '''
    A `mkdir -p` function
    '''
    if not os.path.exists(path):
        os.makedirs(path)
        
def write_file(file_path, id, contents):
    '''
    Write a file in a repo folder.
    
    Arguments:
    file_path -- path of the file in the repo
    id -- id of the biomodel
    contents -- the file contents
    '''
    from _constants import DIR_REPOS
    with open(os.path.join(DIR_REPOS, id, file_path), 'w') as f:
        f.write(contents)
    

def create(id, DIR_REPOS, VERSION):
    '''
    Generates repo contents for a specific model
    '''
    import bioservices
    import _template as t
    s = bioservices.BioModels()

    sbml = s.getModelSBMLById(id)
    mkdirp(os.path.join(DIR_REPOS, id, id))
    
    setup_params = {
        'name': id,
        'version': VERSION,
        'description': '%s from BioModels' % id,
        'url': 'http://www.ebi.ac.uk/biomodels-main/%s' % id
    }
    
    model_params = {
        'path': '%s.xml' % id
    }
    
    init_params = {}
    
    import libsbml
    doc = libsbml.readSBMLFromString(sbml.encode('utf-8'))
    model = doc.getModel()
    notes = h.handle(model.getNotesString().decode('utf-8'))
    
    with open(os.path.join(DIR_REPOS, id, 'setup.py'), 'w') as f:
        f.write(t.setuppy_template(setup_params))
    with open(os.path.join(DIR_REPOS, id, id, 'model.py'), 'w') as f:
        f.write(t.modelpy_template(model_params))
    with open(os.path.join(DIR_REPOS, id, id, id + '.xml'), 'w') as f:
        f.write(sbml.encode('utf-8'))
    with open(os.path.join(DIR_REPOS, id, id, '__init__.py'), 'w') as f:
        f.write(t.initpy_template(init_params))
    with open(os.path.join(DIR_REPOS, id, 'README.md'), 'w') as f:
        f.write(notes.encode('utf-8'))
