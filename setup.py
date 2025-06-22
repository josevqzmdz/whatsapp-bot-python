from setuptools import setup, find_packages
from typing import List

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

# declaring variables for setup functions
PROJECT_NAME = "src"
VERSION = "0.1"
AUTHOR = "chemiloco"
USER_NAME = "josevqzmdz"
AUTHOR_EMAIL = "jose.vqz.mdz@gmail.com"
REPO_NAME = "whatsapp-bot-python"
DESCRIPTION = "this is a simple FAQ whatsapp bot using chatgpt"
REQUIREMENT_FILE_NAME = "requirements.txt"
LICENSE = "MIT"
PYTHON_REQUIRES = ">=3.8"
HYPHEN_E_DOT = "-e ."

def get_requirementes_list() -> List[str]:
    """
        Description:
        this function is going to return list of requirements mentioned in requirements.txt.
        It is also going to return a list which contains names of libraries mentioned in the
        requirements.txt
    """

    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        requirement_list = requirement_file.readlines()
        requirement_list = [requirement_name.replace("\n", "") for requirement_name in requirement_list]
        if HYPHEN_E_DOT in requirement_list:
            requirement_list.remove(HYPHEN_E_DOT)
        return requirement_list

setup(
    name=PROJECT_NAME,
    version=VERSION,
    author=AUTHOR,
    description=DESCRIPTION,
    long_description=long_description,
    url=f"https://github.com/{USER_NAME}/{REPO_NAME}",
    packages=find_packages(),
    license=LICENSE,
    python_requires=PYTHON_REQUIRES,
    install_requires=get_requirementes_list()
)