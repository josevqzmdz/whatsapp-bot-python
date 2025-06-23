from setuptools import setup, find_packages
from typing import List
import os

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

def get_requirementes_list() -> List[str]:
    """
        Description:
        this function is going to return list of requirements mentioned in requirements.txt.
        It is also going to return a list which contains names of libraries mentioned in the
        requirements.txt
    """

    with open(os.environ['REQUIREMENT_FILE_NAME']) as requirement_file:
        requirement_list = requirement_file.readlines()
        requirement_list = [requirement_name.replace("\n", "") for requirement_name in requirement_list]
        if os.environ['HYPHEN_E_DOT'] in requirement_list:
            requirement_list.remove(HYPHEN_E_DOT)
        return requirement_list

    setup(
        name = os.environ['PROJECT_NAME'],
        version = os.environ['VERSION'],
        author = os.environ['AUTHOR'],
        description=os.environ['DESCRIPTION'],
        long_description=os.environ['long_description'],
        url=f"https://github.com/{os.environ['USER_NAME']}/{os.environ['REPO_NAME']}",
        packages=find_packages(),
        license=os.environ['LICENSE'],
        python_requires=os.environ['PYTHON_REQUIRES'],
        install_requires=get_requirementes_list()
    )