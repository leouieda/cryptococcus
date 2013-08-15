from distutils.core import setup


NAME = 'fungui'
FULLNAME = 'FunGui'
DESCRIPTION = "Analyse of microscopy images of Cryptococcus neoformans"
VERSION = '0.1.dev'
with open("README.md") as f:
    LONG_DESCRIPTION = ''.join(f.readlines())
PACKAGES = ['fungui']
AUTHOR = "Leonardo Uieda and Gustavo Braganca"
AUTHOR_EMAIL = 'leouieda@gmail.com'
LICENSE = "BSD License"
URL = "https://github.com/leouieda/fungui"
PLATFORMS = "Any"
SCRIPTS = ['scripts/fungui']
CLASSIFIERS = ["Intended Audience :: End Users/Desktop",
               "Intended Audience :: Science/Research",
               "Topic :: Scientific/Engineering",
               "Programming Language :: Python :: 2.7",
               "License :: OSI Approved :: BSD License",
               "Development Status :: 3 - Alpha",
               "Natural Language :: English"]

if __name__ == '__main__':
    setup(name=NAME,
          fullname=FULLNAME,
          description=DESCRIPTION,
          long_description=LONG_DESCRIPTION,
          version=VERSION,
          author=AUTHOR,
          author_email=AUTHOR_EMAIL,
          license=LICENSE,
          url=URL,
          platforms=PLATFORMS,
          scripts=SCRIPTS,
          packages=PACKAGES,
          classifiers=CLASSIFIERS)

