from setuptools import setup, find_packages

setup(name='{{name}}',
      version={{version}},
      description='{{description}}',
      url='{{url}}',
      maintainer='Stanley Gu',
      maintainer_url='stanleygu@gmail.com',
      packages=find_packages(),
      package_data={'': ['*.xml', 'README.md']},
    )