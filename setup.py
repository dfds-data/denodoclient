#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

requirements = ["pyodbc>4, <5"]

setup_requirements = [
    "pytest-runner",
]

extras_requirements = {"pandas": "pandas>1, <2"}

test_requirements = [
    "pytest>=3",
]

setup(
    author="Martin Morset",
    author_email="mamor@dfds.com",
    python_requires=">=3.8",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    description="Thin high level client to use when consuming data through the Denodo proprietory ODBC driver.",
    install_requires=requirements,
    license="MIT license",
    long_description="See https://github.com/dfds-data/denodoclient/",
    include_package_data=True,
    keywords="denodoclient",
    name="denodoclient",
    packages=find_packages(include=["denodoclient", "denodoclient.*"]),
    setup_requires=setup_requirements,
    extras_require=extras_requirements,
    test_suite="tests",
    tests_require=test_requirements,
    url="https://github.com/dfds-data/denodoclient",
    version="1.0.1",
    zip_safe=False,
)
