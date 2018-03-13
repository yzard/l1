#!/usr/bin/env python

from setuptools import setup

setup(name='l1',
      version='0.1',
      description='L1',
      author='Bugra Akyildiz',
      author_email='vbugra@gmail.com',
      url='bugra.github.io',
      packages=['l1'],
      install_requires=['pandas>=0.16.0',
                        'cvxopt>=1.1.7',
                        'statsmodels>=0.5.0',
                        ]

     )
