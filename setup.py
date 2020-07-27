#!/usr/bin/env python
# -*- coding: utf-8 -*-
import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
  name = 'IPToolz',  
  packages = ['IPToolz'],
  package_dir={'IPToolz': 'IPToolz'},
  package_data={'IPToolz': ['CBit/mo.py','CBit/errors.py']},
              version = '1.1.0',
  license='MIT',    
  description = 'IPToolz is a high-level core python package for Internet Protocol(IP) manipulations.',
  long_description=long_description,
  long_description_content_type="text/markdown",
  author = 'Mobolaji Abdulsalam',                   
  author_email = 'ibraheemabdulsalam@gmail.com',
  url = 'https://github.com/moriire/IPToolz',  
  download_url = 'https://github.com/moriire/IPToolz/archive/v_110.tar.gz',
  keywords = ['IPToolz is a high-level core python package for Internet Protocol(IP) manipulations.'],
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   
    'Programming Language :: Python :: 3',
  ],
   python_requires='>=3.2',
)
