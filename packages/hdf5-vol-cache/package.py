# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)
from spack import *


class Hdf5VolCache(CMakePackage):
    """Package for HDF5 cache VOL."""

    homepage = "https://sdm.lbl.gov/"
    git      = "https://github.com/hpc-io/vol-cache.git"

    maintainers = ['hyoklee']

    version('default', branch='develop')
    version('hyoklee.develop', branch='develop',
            git='https://github.com/hyoklee/vol-cache.git', preferred=True)
    version('local.develop', branch='develop',
            git='file:///home/hyoklee/vol-cache')

    depends_on('hdf5-vol-async')
    
    def cmake_args(self):
        """Populate cmake arguments for HDF5 DAOS."""
        spec = self.spec

        args = [
            '-DBUILD_SHARED_LIBS:BOOL=ON',
            '-DBUILD_TESTING:BOOL=ON'
        ]
        return args
