from setuptools import setup, find_packages

config = {
  "name": "ex47",
  "description": "Description goes here.",
  "author": "Nickunj Chopra (NerdvanaNC)",
  "url": "https://github.com/NerdvanaNC/ex47",
  "download_url": "https://github.com/NerdvanaNC/ex47/archive/refs/heads/main.zip",
  "author_email": "nickunjchopra@gmail.com",
  "version": "0.1",
  "install_requires": ['pytest'],
  "packages": find_packages(exclude=('tests', 'docs')),
  "scripts": []
}

setup(**config)