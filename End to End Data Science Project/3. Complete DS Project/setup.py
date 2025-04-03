from setuptools import find_packages, setup
from typing import List


def get_requirements(file_path:str)-> List[str]:
    with open(file_path, 'r') as file:
        return file.read().splitlines()




setup(
    name='DSProject',
    version='0.0.1',
    author='Dipali',
    author_email='khatuadipsha@gmail.com',
    packages=find_packages(),
    # You may need to uncomment this line if manually specifying requirements
    # install_requires=['numpy', 'pandas', 'scikit-learn', 'matplotlib'], 
    install_requires=get_requirements('requirements.txt')
)
