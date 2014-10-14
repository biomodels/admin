'''
Functions for creating repo contents for a biomodel
'''
import sys
import os
import bioservices
import _template as t

def mkdirp(path):
    '''
    A `mkdir -p` function
    '''
    if not os.path.exists(path):
        os.makedirs(path)

def create(id, DIR_REPOS, VERSION):
    '''
    Generates repo contents for a specific model
    '''
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