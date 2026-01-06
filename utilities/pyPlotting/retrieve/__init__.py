# Copyright (c) 2012-2018, University of Strathclyde
# Authors: Lawrence T. Campbell
# License: BSD-3-Clause

"""
This file is part of Puffin, a multi-frequency FEL code absent of the
averaging / SVEA approximations. This file defines the package for retrieving
data from the Puffin output files.
"""

from .getEnFromInt import getEnFromInt
from .getMagPhase import getMagPhase
from .getPow import getPow
from .getPowFromInt import getPowFromInt
from .process import filterField
from .rawpuffin import getFileSlices, getIntData, getIntFileSlices, getZData, readField

# import readField
# import filterField
# import getMagPhase
