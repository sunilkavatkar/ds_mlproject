from setuptools import setup, find_packages
from typing import List

HIPEN_E_DOT = '-e .'
def get_requirements(file_path: str) -> List[str]:
    """Return cleaned requirements from a requirements file.

    - Strips comments and whitespace
    - Ignores editable installs (lines starting with '-e') and VCS/URL installs
    - Ignores empty lines
    """
    requirements: List[str] = []
    with open(file_path) as file_obj:
        for line in file_obj:
            # remove inline comments and surrounding whitespace
            line = line.split('#', 1)[0].strip()
            if not line:
                continue
            # ignore editable installs and vcs/url entries
            if line.startswith('-e') or line.startswith('git+') or line.startswith('http'):
                continue
            requirements.append(line)
    return requirements

setup(
    name='ds_mlproject',    
    version='0.0.1',
    author='Sunil Kavatkar',
    packages=find_packages(),
    #install_requires=['pandas', 'numpy', 'scikit-learn'],
    install_requires=get_requirements('requirements.txt')
)