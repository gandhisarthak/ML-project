from setuptools import find_packages, setup
from typing import List


hypen_e_dot = "-e ."
def get_requirements(file_path: str) -> list[str]:
    requirenments = []
    with open(file_path) as file_obj:
        requirenments = file_obj.readlines()
        requirenments = [req.replace("\n", "") for req in requirenments]
        if hypen_e_dot in requirenments:
            requirenments.remove(hypen_e_dot)
    return requirenments



        
        













setup(
    name="ml project",
    version="0.0.1",
    author="sarthak gandhi",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt")
)