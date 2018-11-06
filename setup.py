from setuptools import setup, find_packages
import sys


with open('requirements.txt') as f:
    reqs = f.read()

reqs = reqs.strip().split('\n')

install = [req for req in reqs if not req.startswith("git+git://")]
depends = [req.replace("git+git://", "git+http://") for req in reqs if req.startswith("git+git://")]

setup(
    name='lxml',
    version='4.2.4',
    description='lxml for lambda',
    long_description="readme",
    license=license,
    python_requires='>=3.6',
    package_dir={'lxml': 'lxml'},
    packages=['lxml'],
    install_requires=install,
    dependency_links=depends,
)
