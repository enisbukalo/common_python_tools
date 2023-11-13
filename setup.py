from setuptools import setup, find_packages

VERSION = "0.1.0"
DESCRIPTION = "Custom Python Tools."
LONG_DESCRIPTION = "My package to house my commonly used Python tools."

setup(
    name="commnon_tools",
    version=VERSION,
    author="Enis Bukalo",
    author_email="N/A",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=["pytest"],
    url="https://github.com/enisbukalo/common_tools.git",
    license="Apache License 2.0",
    python_requires=">=3.10",
)
