# -*- coding: utf-8 -*-
"""Installer for the yc.facultycv package."""

from setuptools import find_packages
from setuptools import setup

long_description = '\n\n'.join([
    open('README.rst').read(),
    open('CONTRIBUTORS.rst').read(),
    open('CHANGES.rst').read(),
])

setup(
    name='yc.facultycv',
    version='1.7',
    description="An add-on to help YC Faculty enter and submit their CV's.",
    long_description=long_description,
    # Get more from https://pypi.org/classifiers/
    classifiers=[
        "Environment :: Web Environment",
        "Framework :: Plone",
        "Framework :: Plone :: Addon",
        "Framework :: Plone :: 4.3",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
    ],
    keywords='Python Plone',
    author='Rhenne Brown',
    author_email='rbrown12@york.cuny.edu',
    url='https://github.com/collective/yc.facultycv',
    project_urls={
        'PyPI': 'https://pypi.python.org/pypi/yc.facultycv',
        'Source': 'https://github.com/collective/yc.facultycv',
        'Tracker': 'https://github.com/collective/yc.facultycv/issues',
        # 'Documentation': 'https://yc.facultycv.readthedocs.io/en/latest/',
    },
    license='GPL version 2',
    packages=find_packages('src', exclude=['ez_setup']),
    namespace_packages=['yc'],
    package_dir={'': 'src'},
    include_package_data=True,
    zip_safe=False,
    python_requires=">=3.8",
    install_requires=[
        'setuptools',
        'collective.z3cform.datagridfield',
        'z3c.jbot',
        'plone.api>=1.8.4',
        'plone.app.dexterity',
    ],
    extras_require={
        'test': [
            'plone.testing',
        ],
    },
    entry_points="""
    [z3c.autoinclude.plugin]
    target = plone
    [console_scripts]
    update_locale = yc.facultycv.locales.update:update_locale
    """,
)
