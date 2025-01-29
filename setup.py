from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT = "-e ."

def get_requirements(file_path: str) -> List[str]:
    """Reads requirements.txt and returns a list of dependencies."""
    requirements = []
    with open(file_path, "r") as file_obj:
        requirements = file_obj.read().splitlines()  # Read lines and remove \n

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)  # Remove '-e .' if present
    
    return requirements

setup(
    name="ml",
    version="0.0.1",
    author="Prateek",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt")
)
