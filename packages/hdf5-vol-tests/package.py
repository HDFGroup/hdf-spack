# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Hdf5VolTests(CMakePackage):
    """This package tests HDF5 Virtual Object Layer (VOL)."""

    homepage = "https://www.hdfgroup.org"
    git      = "https://github.com/HDFGroup/vol-tests"

    maintainers = ['hyoklee']

    version('master', preferred=True)
    variant('vol-async', default=True, description='Enable async VOL')
    variant('vol-cache', default=False, description='Enable cache VOL')
    variant('vol-external-passthrough', default=False, 
            description='Enable external pass-through VOL')

    variant('async', default=True, description='Enable parallel tests.')
    variant('parallel', default=True, description='Enable async API tests.')
    variant('part', default=True, 
            description='Enable building the main test executable.')
    depends_on('szip', when='+parallel')
    depends_on('hdf5-vol-async', when='+vol-async')
    depends_on('hdf5-vol-cache', when='+vol-cache')
    depends_on('hdf5-vol-external-passthrough', 
               when='+vol-external-passthrough')

    def cmake_args(self):
        args = []
        if '+parallel' in self.spec:
            args.append('-DHDF5_VOL_TEST_ENABLE_PARALLEL:BOOL=ON')
        if '+async' in self.spec:
            args.append('-DHDF5_VOL_TEST_ENABLE_ASYNC:BOOL=ON')
        if '+part' in self.spec:
            args.append('-DHDF5_VOL_TEST_ENABLE_PART:BOOL=ON')
        return args
