#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2017-2020 Pyresample developers.
#
# This file is part of Pyresample
#
# Author(s):
#
#   Panu Lahtinen <panu.lahtinen@fmi.fi>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""Code for resampling using bilinear algorithm for irregular grids.

The algorithm is taken from

http://www.ahinson.com/algorithms_general/Sections/InterpolationRegression/InterpolationIrregularBilinear.pdf

"""

import warnings

from ._numpy_resampler import (  # noqa: F401
    resample_bilinear,
    get_sample_from_bil_info,
    get_bil_info,
    NumpyBilinearResampler,
)
try:
    from .xarr import (  # noqa: F401
        XArrayBilinearResampler,
        CACHE_INDICES,
    )
except ImportError:
    warnings.warn("XArray and/or zarr not found, XArrayBilinearResampler won't be available.")
    XArrayBilinearResampler = None
    CACHE_INDICES = None


class XArrayResamplerBilinear(XArrayBilinearResampler):
    """Wrapper for the old resampler class."""

    def __init__(self, source_geo_def,
                 target_geo_def,
                 radius_of_influence,
                 **kwargs):
        """Initialize resampler."""
        warnings.warn("Use of XArrayResamplerBilinear is deprecated, use XArrayBilinearResampler instead")

        super(XArrayResamplerBilinear, self).__init__(
            source_geo_def,
            target_geo_def,
            radius_of_influence,
            **kwargs)


class NumpyResamplerBilinear(NumpyBilinearResampler):
    """Wrapper for the old resampler class."""

    def __init__(self, source_geo_def,
                 target_geo_def,
                 radius_of_influence,
                 **kwargs):
        """Initialize resampler."""
        warnings.warn("Use of NumpyResamplerBilinear is deprecated, use NumpyBilinearResampler instead")

        super(NumpyResamplerBilinear, self).__init__(
            source_geo_def,
            target_geo_def,
            radius_of_influence,
            **kwargs)
