# -*- coding: utf-8 -*-
"""
Created on Sun Feb  9 18:17:09 2020

@author: Ayush Garg
"""

from distutils.core import setup
setup(
  name = 'outliers_detection_101703129',
  packages = ['outliers_detection_101703129'],
  version = '0.1',
  license='MIT',
  description = 'You can find the outliers in your dataset with the hep of this library.',
  author = 'Ayush Garg',
  author_email = '987ayush@gmail.com',
  url = 'https://github.com/ayush7garg/outliers_detection_101703129',
  download_url = 'https://github.com/ayush7garg/outliers_detection_101703129/archive/v_01.tar.gz',
  install_requires=[
          'numpy',
          'pandas',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.7',
  ],
)