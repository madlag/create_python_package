# -*- coding: utf-8 -*-
from setuptools import setup


def readme():
    with open('README.rst') as f:
        return f.read()

setup(name='create_python_package',
      version='0.1',
      description='Python module creating utility',
      long_description=readme(),
      classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
        'Topic :: Programming Language :: Python :: 3',
      ],
      keywords='utility, package',
      url='',
      author='François Lagunas',
      author_email='francois.lagunas@m4x.org',
      license='MIT',
      packages=['create_python_package'],
      install_requires=[
          'jinja2', 'click', 'sh'
      ],
      test_suite='nose.collector',
      tests_require=['nose', 'nose-cover3'],
      entry_points={
          'console_scripts': ['create_python_package=create_python_package:run'],
      },
      include_package_data=True,
      zip_safe=False)
