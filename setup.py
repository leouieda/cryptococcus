import os
from setuptools import setup, find_packages

NAME = "cryptococcus"

# Get version and release info
with open(os.path.join(NAME, '_version.py')) as f:
    exec(f.read())
# Use the README for the long description
with open('README.rst') as f:
    long_description = f.read()

VERSION = __version__
AUTHOR = "Leonardo Uieda"
AUTHOR_EMAIL = "leouieda@gmail.com"
MAINTAINER = AUTHOR
MAINTAINER_EMAIL = AUTHOR_EMAIL
DESCRIPTION = ''
LONG_DESCRIPTION = long_description
URL = "http://github.com/leouieda/{}".format(NAME)
LICENSE = "BSD 3-clause"
PLATFORMS = "OS Independent"
PACKAGES = find_packages()
PACKAGE_DATA = {os.path.join(NAME, 'datasets'): [os.path.join('data', '*')]}
REQUIRES = ["numpy"]
CLASSIFIERS = ["Development Status :: 3 - Alpha",
               "Environment :: Console",
               "Intended Audience :: Science/Research",
               "License :: OSI Approved :: {} License".format(LICENSE),
               "Operating System :: {}".format(PLATFORMS),
               "Programming Language :: Python 3.5",
               "Topic :: Scientific/Engineering"]


if __name__ == '__main__':
    setup(name=NAME,
          maintainer=MAINTAINER,
          maintainer_email=MAINTAINER_EMAIL,
          description=DESCRIPTION,
          long_description=LONG_DESCRIPTION,
          url=URL,
          license=LICENSE,
          classifiers=CLASSIFIERS,
          author=AUTHOR,
          author_email=AUTHOR_EMAIL,
          platforms=PLATFORMS,
          version=VERSION,
          packages=PACKAGES,
          package_data=PACKAGE_DATA,
          install_requires=REQUIRES)
