# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Hdf5VolExternalPassthrough(CMakePackage):
    """Package for HDF5 external pass-through VOL."""

    homepage = "https://sdm.lbl.gov/"
    git      = "https://github.com/hpc-io/vol-external-passthrough.git"

    maintainers = ['hyoklee']

    version('default', branch='async_vol_register_optional')
    
    depends_on('hdf5-hpc-io')
    
    def cmake_args(self):
        """Populate cmake arguments for HDF5 DAOS."""
        spec = self.spec

        args = [
            '-DBUILD_SHARED_LIBS:BOOL=ON',
            '-DBUILD_TESTING:BOOL=ON'
        ]
        return args
