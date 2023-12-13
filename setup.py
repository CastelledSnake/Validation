from setuptools import setup, find_packages

setup(
    name="ENSTA Validation",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "pytest",
        # Add other dependencies here
    ],
)
