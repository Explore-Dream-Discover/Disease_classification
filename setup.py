import setuptools
from setuptools import find_packages
with open("README.md","r",encoding='utf-8') as f:
    long_desc=f.read()


__version__="0.0.0"

REPO_NAME="Disease_classification"
AUTHOR_USER_NAME="Explore-Dream-Discover"
SRC_REPO="CnnClassifier"
AUTHOR_EMAIL="elangopavankumar@gmail.com"


setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A Small app",
    long_description=long_desc,
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    package_dir={"":"src"},
    packages=find_packages(where="src")
)