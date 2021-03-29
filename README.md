This holds a Spack package to build HDF5 using CMake .  
It relies on Spack and the builtin Spack packages, some of which may be overridden by this repo.

## Getting started

Initial setup like:

```bash
cd /path/your-working-dir
git clone https://github.com/HDFGroup/hdf-spack
git clone https://github.com/spack/spack.git
./spack/bin/spack repo add hdf-spack

