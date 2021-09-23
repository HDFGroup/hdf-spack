# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *

class Hdf5VolAsync(CMakePackage):
    """This package enables asynchronous IO in HDF5."""

    homepage = "https://sdm.lbl.gov/"
    git      = "https://github.com/hpc-io/vol-async"
    maintainers = ['hyoklee']

    version('develop', branch='develop')
    version('hyoklee.develop',
            branch='develop',
            git='https://github.com/hyoklee/vol-async', preferred=True)
    version('local.develop', branch='develop',
            git='file:///scr/hyoklee/src/vol-async')

    depends_on('argobots@main')
    depends_on('hdf5-hpc-io')
    # Use the following if you want to use HDFGroup/hdf5@develop-1.3 instead.
    # depends_on('hdf5@develop-1.13+mpi+threadsafe')

    # These are for testing with the generic 'make' command.
    # patch('Makefile.patch')
    # patch('src_Makefile.patch')
    # patch('test_Makefile.patch')
    def cmake_args(self):
        """Populate cmake arguments for HDF5 VOL."""
        spec = self.spec

        args = [
            '-DBUILD_SHARED_LIBS:BOOL=ON',
            '-DBUILD_TESTING:BOOL=ON'
            '-DCMAKE_C_COMPILER=mpicc',
            '-DCMAKE_CXX_COMPILER=mpicxx',
        ]

        return args
    

    def setup_environment(self, spack_env, run_env):
        spack_env.set('HDF5_PLUGIN_PATH', self.build_directory+'/lib')
        spack_env.set('HDF5_VOL_CONNECTOR',
                         'async under_vol=0\;under_info={}')        
        spack_env.set('LD_PRELOAD', self.spec['argobots'].prefix+'/lib/libabt.so')
        
