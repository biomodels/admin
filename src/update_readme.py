'''
Script to update README file
'''

from _create import write_file, mkdirp
from _template import render_template, read_file
from _shell import shell
from _remove import remove
from _constants import FILE_REPO_LIST, DIR_REPOS, PATH_README_TEMPLATE
import html2text
h = html2text.HTML2Text()
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
    
    # Read SBML Content
    sbml = read_file(os.path.join(DIR_REPOS, id, id, id + '.xml'))
    import libsbml
    doc = libsbml.readSBMLFromString(sbml)
    model = doc.getModel()
    notes = h.handle(model.getNotesString().decode('utf-8'))
    
    # Set up parameters for rendering in template
    params = {
        'id': id,
        'model_id': model.getId(),
        'notes': notes 
        }
    
    readme_content = render_template(PATH_README_TEMPLATE, params).encode('utf-8')
    
    write_file('README.md', id, readme_content)
    shell(cmd='git add README.md',
          dir=os.path.join(DIR_REPOS, id))
    shell(cmd=['git', 'commit', '-am', 'Updated README'],
          dir=os.path.join(DIR_REPOS, id))
    shell(cmd=['git', 'push'],
          dir=os.path.join(DIR_REPOS, id))