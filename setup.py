from setuptools import setup
from setuptools import find_packages


setup(
    name='markdown-urlize',
    version='1.0.0',
    description="A python-markdown extension for linkifying inline urls",
    maintainer='Kit Sunde',
    maintainer_email='kitsunde@gmail.com',
    url='https://github.com/Celc/markdown-urlize',
    packages=['mdx_urlize'],
    package_dir={'mdx_urlize': 'src/mdx_urlize'},
)