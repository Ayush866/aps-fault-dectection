from setuptools import find_packages,setup

REQURIMENT_FILE_NAME = "requirements.txt"
HYPHEN_E_DOT = "-e ."
def get_requriments():
    with open(REQURIMENT_FILE_NAME) as requirement_file:
        requirement_list = requirement_file.readline()
        requirement_list = [requirement_name.replace("\n","") for requirement_name in requirement_list]

    if HYPHEN_E_DOT in requirement_list:
        requirement_list.remove(HYPHEN_E_DOT)
    return requirement_list
setup(
    name="sensor",
    version="0.0.1",
    author="Ayush",
    author_email="ayush786bisht@gmail.com",
    packages=find_packages(),
    install_requires = get_requriments(),
)