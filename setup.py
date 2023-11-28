from os import path
from setuptools import setup, find_packages

# Version Number
module_name = 'flask_errors'
module_path = path.join(module_name, '__init__.py')
version_line = [line for line in open(
    module_path, 'r') if line.startswith('__version__')][0]
v = version_line.split('__version__ = ')[-1]
st = v.index('\'')
__version__ = v[st + 1: v.index('\'', st + 1)]

# Readme
with open('README.md', 'r') as file:
    long_description = file.read()

# Run
setup(
    name=module_name,
    version=__version__,
    description='Flask error handlers',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/JonathanHiggs/flask_errors',
    author='Jonathan Higgs',
    author_email='jonathan.higgs.11@mail.wbs.ac.uk',
    packages=find_packages(),
    install_requires=['Flask>2.2.5'],
    zip_safe=True)
