#!/bin/bash

conda create -y -n puffin compilers openmpi hdf5=*=mpi_openmpi* fftw=*=mpi_openmpi* cmake doxygen
conda activate puffin

set -xe

cmake -B build .
make -C build -j8

cp -f build/source/puffin $CONDA_PREFIX/bin
