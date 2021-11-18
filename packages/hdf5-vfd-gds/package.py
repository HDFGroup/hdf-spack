# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *

class Hdf5VfdGds(CMakePackage, CudaPackage):
    """This pacakge enables GPU Direct Storage Virtual File Driver in HDF5."""

    # Package info
    homepage    = 'https://github.com/hpc-io/vfd-gds'
    url = 'https://github.com/hpc-io/vfd-gds/archive/refs/tags/1.0.0.tar.gz'
    git         = 'https://github.com/hpc-io/vfd-gds.git'
    maintainers = ['hyoklee', 'lrknox']

    # Versions
    version('master', branch='master')
    version('1.0.0', sha256='6b16105c7c49f13fc05784ee69b78d45fb159270c78d760689f9cd21e230ddd2', default=True)
    
    # Dependencies
    depends_on('cuda')    
    depends_on('cmake@3.12:')
    depends_on('hdf5@develop-1.13')    


    def cmake_args(self):
        spec = self.spec

        # CMake options
        args = [
            self.define('BUILD_TESTING', self.run_tests),
        ]

        return args
