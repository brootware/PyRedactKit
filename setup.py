#!/usr/bin/env python
from importlib.metadata import entry_points
from platform import platform


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="pyredactkit",
    version="1.0.0",
    description="Python bot for mouse event simulation",
    license="GNU",
    author="Oaker Min",
    author_email="ominbruce@outlook.com",
    maintainer="Oaker Min",
    maintainer_email="ominbruce@outlook.com",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/brootware/PyRedactKit.git",
    packages=["src"],
    py_modules=["redact", "src.redactor"],
    install_requires=[],
    platforms="any",
    entry_points="""
    [console_scripts]
    pyredactkit=mousebot:main
    """,
)
