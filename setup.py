#! /usr/bin/env python3
# Copyright (c) 2021 Sebastian Pipping <sebastian@pipping.org>
# Licensed under the MIT license

from setuptools import find_packages, setup

setup(
    name='srisum',
    version='1.0.1',
    license='MIT',
    description='Compute and display subresource integrity (SRI) checksums',
    long_description=open('README.md', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    author='Sebastian Pipping',
    author_email='sebastian@pipping.org',
    url='https://github.com/hartwork/srisum',
    python_requires='>=3.6',
    setup_requires=[
        'setuptools>=38.6.0',  # for long_description_content_type
    ],
    install_requires=[
        'requests',
    ],
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'srisum = srisum.__main__:main',
        ],
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Software Development',
        'Topic :: System :: Archiving :: Packaging',
        'Topic :: Text Processing :: Markup :: HTML',
        'Topic :: Utilities',
    ],
)
