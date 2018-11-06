from setuptools import setup

setup(
    name='lxml',
    version='4.2.5',
    description='lxml for lambda',
    long_description="readme",
    license=license,
    python_requires='>=3.6',
    packages=['lxml'],
    include_package_data=True,
    package_data={
      'lxml': ['*']
    }
)
