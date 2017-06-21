# -*- coding: utf-8 -*-
"""Installer for the akbild.behavior.colorscheme package."""

from setuptools import find_packages
from setuptools import setup


long_description = '\n\n'.join([
    open('README.rst').read(),
    open('CONTRIBUTORS.rst').read(),
    open('CHANGES.rst').read(),
])


setup(
    name='collective.permalink',
    version='1.0.0.dev0',
    description='Show a new link (permalink) in Plone contents. '
                'This will not change if you move the content itself.',
    long_description=long_description,
    # Get more strings from
    # http://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Framework :: Plone',
        'Framework :: Plone :: 5.0',
        'Framework :: Plone :: 5.1',
        'Programming Language :: Python',
    ],
    keywords='plone plonegov permalink',
    author='RedTurtle Technology',
    author_email='sviluppoplone@redturtle.it',
    url='http://plone.org/products/collective.permalink',
    license='GPL',
    packages=find_packages(exclude=['ez_setup']),
    namespace_packages=['collective'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'setuptools',
        'plone.uuid',
    ],
    extras_require={
        'test': [
            'plone.app.testing',
            'plone.app.contenttypes',
        ],
    },
    entry_points="""
    [z3c.autoinclude.plugin]
    target = plone
    """,
)
