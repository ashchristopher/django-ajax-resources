import os
from setuptools import setup, find_packages

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='django-ajax-resources',
    version='0.1.0',
    packages = find_packages(),
    author='Ash Christopher',
    author_email='ash@newthink.net',
    description='Django library that provides the simplest of ajax resource endpoints.',
    license='LICENSE.txt',
    url='http://github.com/ashchristopher/django-ajax-resources',
    keywords='django ajax resource endpoint',
    long_description=read('README'),
    install_requires = ['decorator>=3.3'], # i used 3.3.1, so I picked 3.3 arbitrarily.    
)
