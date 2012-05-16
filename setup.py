from setuptools import setup
from setuptools import find_packages


setup(
    name='markdown-urlize',
    version='1.0.2',
    description="A python-markdown extension for linkifying inline urls",
    maintainer='Datadog, Inc.',
    maintainer_email='packages@datadoghq.com',
    url='https://github.com/Datadog/markdown-urlize',
    install_requires=[],
    setup_requires=[],
    packages=find_packages(),
)
