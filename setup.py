#!/usr/bin/env python
from importlib.metadata import entry_points
from platform import platform


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

readme = ""

setup(
    name="pyredactkit",
    version="1.0.0",
    long_description=readme,
    description="Python bot for mouse event simulation",
    python_requires="==3.*,>=3.6.0",
    license="GNU",
    author="Oaker Min",
    author_email="ominbruce@outlook.com",
    maintainer="Oaker Min",
    maintainer_email="ominbruce@outlook.com",
    packages=["src"],
    py_modules=["pyredactkit", "src.redact"],
    install_requires=[
        "attrs == 21.*,>=21.4.0",
        "click == 8.*>=8.1.2",
        "iniconfig == 1.*,>=1.1.1",
        "joblib == 1.*,>=1.1.0",
        "nltk == 3.7"
    ],
    extras_requires={
        "dev": ["packaging == 21.3",
                "pluggy == 1.0.0",
                "py == 1.11.0",
                "pyparsing == 3.0.8",
                "pytest == 7.1.1",
                "regex == 2022.3.15",
                "tomli == 2.0.1",
                "tqdm == 4.64.0"]
    },
    platforms="any",
    entry_points="""
    [console_scripts]
    pyredactkit=pyredactkit:main
    """,
)
