from setuptools import setup, find_packages

setup(
    name="petclinic",
    version="1.0.0",
    packages=find_packages(),
    python_requires=">=3.11",
    install_requires=["django>=6.0"],
)
