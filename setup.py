from setuptools import setup, find_packages
from typing import List

HYPHEN_E_DOT = "-e ."

def get_requirements(file_path:str) -> list[str]:
    """
    This function returns the list of requirements from the given file path.
    """
    requirements=[]
    with open(file_path) as fileobj:
        requirments=fileobj.readlines()
        requirements = [req.replace("\n","") for req in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)

    return requirements

setup(
    name='mlprojectE2E',
    version='0.1',
    packages=find_packages(),
    author='Nikhil',
    description='A machine learning project for end-to-end pipeline',
    install_requires= get_requirements('requirements.txt')
)