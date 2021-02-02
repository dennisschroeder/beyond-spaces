# -*- coding: utf-8 -*-


"""setup.py: setuptools control."""

import re
from setuptools import setup

version = re.search(
    '^__version__\s*=\s*"(.*)"',
    open('core/core.py').read(),
    re.M
).group(1)

with open("README.rst", "rb") as f:
    long_descr = f.read().decode("utf-8")

setup(
    name="beyond-spaces",
    packages=["core"],
    install_requires=['Click', 'applescript', 'undictify', 'ruamel.yaml'],
    entry_points={
        "console_scripts": ['beyond-spaces = core.core:main', 'bs = core.core:main']
    },
    version=version,
    description="Python command line application to manage macOS workspaces and handle applications.",
    long_description=long_descr,
    author="Dennis Schröder",
    author_email="dennisschroeder@me.com",
    url="https://github.com/dennisschroeder",
)
