#setup.py
from setuptools import setup, find_packages
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text('utf-8')

setup(
    name='picklerpc',
    version='0.1.0',
    packages=find_packages(include=['picklerpc*']),
    author='chenxf',
    author_email='cxf529125853@163.com',
    url='https://github.com/ptrajdos/picklerpc',
    long_description=long_description,
    long_description_content_type='text/markdown',

    python_requires='>=3.6',
)
