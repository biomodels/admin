from setuptools import setup, find_packages

version = '0.0.0'

setup(name='biomodels-admin',
      version=version,
      description='Admin tools for biomodels repos',
      author='Stanley Gu',
      author_email='stanleygu@gmail.com',
      url='https://github.com/stanleygu/rename',
      packages=find_packages(),
      install_requires=[
        'jinja2',
        'bioservices',
        'six',
        'PyGithub'
      ]
      )