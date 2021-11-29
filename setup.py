from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

with open(path.join(here, 'requirements.txt'), encoding='utf-8') as f:
    requires = f.read().split()

setup(
    name='knowledgelab',
    version='0.0.2',
    description='Knowledge Repo integration for JupyterLab',
    long_description=long_description,
    url='https://github.com/timkpaine/knowledgelab',
    download_url='https://github.com/timkpaine/knowledgelab/archive/v0.0.2.tar.gz',
    author='Tim Paine, Ramindu Deshapriya',
    author_email='t.paine154@gmail.com, rasade88@gmail.com',
    license='Apache 2.0',
    install_requires=requires,
    extras_require={'dev': requires + ['pytest', 'pytest-cov', 'pylint', 'flake8', 'mock', 'codecov']},
    python_requires=">=3.7",
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",

    ],

    keywords='analytics jupyter',
    packages=find_packages(exclude=['tests']),
    zip_safe=False,
)
