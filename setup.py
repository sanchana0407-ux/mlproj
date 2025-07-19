from setuptools import find_packages, setup
from typing import List


def get_requirements(file_path: str)-> List[str]:
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.strip() for req in requirements if req.strip() and not req.strip().startswith('-e')]        
        
    return requirements
        

setup(
name = 'mlproj',version ='0.0.1',author='sanchana', author_email = 'sanchana0407@gmail.com', 
packages= find_packages(),#install_requires = ['pandas','numpy','seaborn']
install_requires = get_requirements('requirements.txt')
)



