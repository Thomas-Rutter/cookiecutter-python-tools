"""Setup module for package."""
from pathlib import Path

from setuptools import find_packages, setup


def get_version():
    """Get the version from the __init__.py file.

    Returns:
        str: The version.
    """
    init_file = Path("./src/{{cookiecutter.module_name}}/__init__.py")
    with open(init_file, "r") as read_file:
        lines = read_file.readlines()
    for line in lines:
        if line.startswith("__version__ ="):
            return line.split('"')[1]


NAME = "{{cookiecutter.project_id}}"
VERSION = get_version()

setup(
    name=NAME,
    version=VERSION,
    package_dir={'': 'src'},
    packages=find_packages('src'),
    command_options={
        'build_sphinx': {
            'project': ('setup.py', NAME),
            'version': ('setup.py', VERSION),
            'release': ('setup.py', VERSION),
            'source_dir': ('setup.py', 'docs')
        }
    },
    # entry_points={
    #     'console_scripts': [
    #         'name = {{cookiecutter.module_name}}.core:main'
    #     ]
    # },
)
