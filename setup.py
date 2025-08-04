from setuptools import setup, find_packages

setup(
    name="api-tests",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "pytest==7.4.0",
        "requests==2.31.0",
        "pytest-html==3.2.0"
    ]
)
