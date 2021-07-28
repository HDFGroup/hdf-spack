# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)
from spack import *


class Hdf5VolRest(CMakePackage):
    """The HDF5 REST VOL connector is a plugin for HDF5 designed with the goal of
allowing HDF5 applications to utilize web-based storage systems by translating
HDF5 API calls into HTTP-based REST calls, as defined by the HDF5 REST API."""

    homepage = "https://hdfgroup.org"
    url      = "https://github.com/HDFGroup/vol-rest"

    maintainers = ['hyoklee']
    version('master',
            git='https://github.com/HDFGroup/vol-rest.git',
            submodules=True)
    version('hdf5_1_12_update',
            git='https://github.com/HDFGroup/vol-rest.git',
            branch='hdf5_1_12_update',
            submodules=True)
    version('hyoklee.hdf5_1_12_update', preferred=True,
            branch='hdf5_1_12_update',
            git='https://github.com/hyoklee/vol-rest.git',
            submodules=True)

    depends_on('cmake')
    depends_on('curl')
    depends_on('yajl')

    
