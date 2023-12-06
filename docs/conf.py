# Copyright 2023  Projektpraktikum Python.
# SPDX-License-Identifier: Apache-2.0
"""Sphinx config."""

project = 'example'
copyright = '2023, Projektpraktikum Python'  # noqa: A001
author = 'Projectpraktikum Python'

autoapi_python_use_implicit_namespaces = True
autodoc_typehints = 'description'

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx_autodoc_typehints',
]

html_theme = 'sphinx_rtd_theme'
