'''the setup file is an essential part of package and
distributing python project .its is used in by setuptools 
(or distributed in older Python version )
to define the configuration of your project such as
its metdata , dependencies and more '''

from setuptools import find_packages, setup
from typing import List 

def get_requirements() -> List[str]:
    """
    this function will return list of requiredment
    
    """
    requirement_lst:List[str]=[]       
    try:
        with open('requirements.txt','r') as file:
            #read line from the file
            lines= file.readlines()
            ##process each lines:
            for line in lines:
                requirement = line.strip()
                ## ignore empty lines and -e
                if requirement and requirement != '-e .':
                    requirement_lst.append(requirement)
    except FileNotFoundError:
        print("requirements.txt file now found")
    return requirement_lst     
print(get_requirements())

setup(
    name= "NetworkSecurity",
    version= '0.0.1',
    author= "Devesh Srivastava",
    author_email = "vicky16debu@gmail.com",
    install_requires =get_requirements()
)