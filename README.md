This holds a Spack package to build HDF5 using CMake .  
It relies on Spack and the builtin Spack packages, some of which may be overridden by this repo.

## Getting started

Initial setup for bash:

cd /path/your-working-dir
git clone https://github.com/spack/spack.git
git clone https://github.com/HDFGroup/hdf-spack
source ../spack/share/spack/setup-env.sh
spack repo add hdf-spack
spack repo list
