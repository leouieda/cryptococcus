#!/bin/bash

hash -r
echo $MINICONDA_URL
wget $MINICONDA_URL -O miniconda.sh;
bash miniconda.sh -b -f -p $MINICONDA;
conda config --set always_yes yes
conda update conda
conda info -a
