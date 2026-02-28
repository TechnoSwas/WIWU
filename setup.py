from setuptools import setup, find_packages

setup(
    name="WIWU",
    version="1.0.0",
    description="A simple music library - make music with notes like C4, A#3!",
    author="TechnoSwas",
    packages=find_packages(),
    install_requires=[
        "numpy",
    ],
)