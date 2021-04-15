This holds a Spack package to build HDF5 using CMake .  
It relies on Spack and the builtin Spack packages, some of which may be overridden by this repo.

## Getting started

Initial setup for bash:

cd /path/your-working-dir

git clone https://github.com/spack/spack.git

git clone https://github.com/HDFGroup/hdf-spack

source ./spack/share/spack/setup-env.sh

spack repo add ./hdf-spack

spack repo list

spack <spec, install, uninstall> <package>

The hdf-spack repository contains files for two spack packages:  hdf5 and hdf5-cmake.
The hdf5 package is an update to the hdf5 package in the official spack repository
that switches from Autotools to CMake for building HDF5.  Changes can be seen in the
pull request:  https://github.com/spack/spack/pull/18937.

The hdf5-cmake package has most of those updates and also has new variants to enable
these compression filters:
    blosc bshuf bz2 jpeg lz4 lzf szf
    zfp zstd bitgroom mafisc pv av cv
These filters are enabled by default.

References: 

https://spack.readthedocs.io/en/latest/repositories.html#
https://github.com/spack/spack/pull/18937

