# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

# ----------------------------------------------------------------------------
#     spack install remora
#
# You can edit this file again by typing:
#
#     spack edit remora
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
    git = "git@github.com:seahorce-scidac/REMORA.git"
    version("development", branch="development", submodules=True) 

    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    maintainers("jmsexton03", "hklion", "asalmgren", "iulian787")

    # FIXME: Add the SPDX identifier of the project's license below.
    # See https://spdx.org/licenses/ for a list. Upon manually verifying
    # the license, set checked_by to your Github username.
    license("LGPL-3.0-or-later", checked_by="iulian787")

    version("0.9", sha256="c2dec85877daea6e8c392ffff1ea86d22965ff021f0c0a1019d74936328ea40d")

    variant("doc", default=False, description="Build documentation") # option(REMORA_ENABLE_DOCUMENTATION "Build documentation" OFF)
    variant("warnings", default=False, description="Enable all compiler warnings") # option(REMORA_ENABLE_ALL_WARNINGS  "Enable all compiler warnings" OFF)
    variant("tests", default=False, description="Enable regression and unit tests") # option(REMORA_ENABLE_TESTS         "Enable regression and unit tests" OFF)
    variant("netcdf", default=False, description="Enable NetCDF IO") # option(REMORA_ENABLE_NETCDF        "Enable NetCDF IO" OFF)
    # option(REMORA_ENABLE_HDF5          "Enable HDF5 IO" ${REMORA_ENABLE_NETCDF})
    # option(REMORA_ENABLE_FCOMPARE "Enable building fcompare when not testing" OFF)

#Options for performance
    variant("mpi", default=False, description="Enable MPI ")      # option(REMORA_ENABLE_MPI    "Enable MPI"    OFF)
    variant("openmp", default=False, description="Enable OpenMP") # option(REMORA_ENABLE_OPENMP "Enable OpenMP" OFF)
    variant("cuda", default=False, description="Enable CUDA")     # option(REMORA_ENABLE_CUDA   "Enable CUDA"   OFF)
    variant("hip", default=False, description="Enable HIP")       # option(REMORA_ENABLE_HIP    "Enable HIP"    OFF)
    variant("sycl", default=False, description="Enable SYCL")     # option(REMORA_ENABLE_SYCL   "Enable SYCL"   OFF)

    depends_on("cmake", type="build")

    depends_on("netcdf-c build_system=cmake")

    depends_on("mpi", when="+mpi")
    depends_on("cuda", when="+cuda")

    def cmake_args(self):
        args = [
            self.define_from_variant("REMORA_ENABLE_DOCUMENTATION", "doc"),
            self.define_from_variant("REMORA_ENABLE_ALL_WARNINGS", "warnings"),
            self.define_from_variant("REMORA_ENABLE_TESTS", "tests"),
	    self.define_from_variant("REMORA_ENABLE_MPI", "mpi"),
	    self.define_from_variant("REMORA_ENABLE_OPENMP", "openmp"),
	    self.define_from_variant("REMORA_ENABLE_CUDA", "cuda")
	]
        return args
