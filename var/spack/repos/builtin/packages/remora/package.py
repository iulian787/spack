# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

# ----------------------------------------------------------------------------
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
# This is a template package file for Spack.  We've put "FIXME"
# next to all the things you'll want to change. Once you've handled
# them, you can save this file and test your package like this:
#
#     spack install remora
#
# You can edit this file again by typing:
#
#     spack edit remora
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack.package import *


class Remora(CMakePackage):
    """
    REMORA is currently under development as a next-generation version of the Regional Ocean Modeling System (ROMS).
      REMORA is built on AMReX, an adaptive mesh refinement software framework, which provides the underlying software
      infrastructure for block structured AMR operations.
     REMORA is designed to run on machines from laptops to multicore CPU and hybrid CPU/GPU systems.
     This documentation is currently under development, there are detailed resources available on the
     ROMS Documentation Portal for the Regional Ocean Modeling System.
    """

    homepage = "https://roms-x.readthedocs.io/en/latest/index.html`"

    url = "https://github.com/iulian787/REMORA/archive/refs/tags/r0.9.tar.gz"
    git = "https://github.com/iulian787/REMORA.git"
    version("development", branch="development", submodules=True) 

    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    maintainers("jmsexton03", "hklion", "asalmgren", "iulian787")

    # FIXME: Add the SPDX identifier of the project's license below.
    # See https://spdx.org/licenses/ for a list. Upon manually verifying
    # the license, set checked_by to your Github username.
    license("LGPL-3.0-or-later", checked_by="iulian787")

    version("0.9", sha256="c2dec85877daea6e8c392ffff1ea86d22965ff021f0c0a1019d74936328ea40d")

    # FIXME: Add dependencies if required.

    variant("mpi", default=True, description="Enable parallel ")

    depends_on("cmake", type="build")

    depends_on("netcdf-c build_system=cmake")

    depends_on("mpi", when="+mpi")

    def cmake_args(self):
        # FIXME: Add arguments other than
        # FIXME: CMAKE_INSTALL_PREFIX and CMAKE_BUILD_TYPE
        # FIXME: If not needed delete this function
        args = []
        return args
