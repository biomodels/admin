# {{id}}: {{model_id}}

## Installation

Download this repository, and install with distutils

`python setup.py install`

Or, install using pip

`pip install git+https://github.com/biomodels/{{id}}.git`

To install a specific version (in this example, from the 2014-09-16 BioModels release)

`pip install git+https://github.com/biomodels/{{id}}.git@20140916`

{% if notes %}
# Model Notes
{{notes}}
{% endif %}