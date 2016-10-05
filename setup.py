#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'ansicolors>=1.0.2',
    'Click>=6.0',
    'PyYAML>=3.12',
    'requests>=2.11.1'
]

setup(
    name='pypertrail',
    version='1.0.0',
    description="Python wrapper library and CLI for papertrail API.",
    long_description=readme + '\n\n' + history,
    author="Quentin Rousseau",
    author_email='contact@quent.in',
    url='https://github.com/kwent/pypertrail',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'pypertrail=pypertrail.cli:main'
        ]
    },
    include_package_data=True,
    install_requires=requirements,
    license="MIT license",
    zip_safe=False,
    keywords='pypertrail',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Software Development',
        'Topic :: System :: Logging',
        'Topic :: System :: Monitoring'
    ],
    test_suite='tests'
)
