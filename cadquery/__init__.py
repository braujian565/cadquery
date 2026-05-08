"""CadQuery - A parametric 3D CAD scripting framework built on top of OCCT.

CadQuery is an intuitive, easy-to-use Python module for building parametric
3D CAD models. It is well suited to scripting and design automation.

Example usage::

    import cadquery as cq

    # Create a simple box
    result = cq.Workplane("XY").box(10, 10, 5)

    # Export to STEP
    cq.exporters.export(result, "box.step")

    # Export to STL for 3D printing
    cq.exporters.export(result, "box.stl")
"""

from .cq import Workplane, CQContext
from .occ_impl.geom import Vector, Matrix, Plane, BoundBox
from .occ_impl.shapes import (
    Shape,
    Vertex,
    Edge,
    Wire,
    Face,
    Shell,
    Solid,
    Compound,
    CompSolid,
)
from .occ_impl.assembly import Assembly, ConstraintKind
from .selectors import (
    NearestToPointSelector,
    ParallelDirSelector,
    DirectionSelector,
    PerpendicularDirSelector,
    TypeSelector,
    RadiusNthSelector,
    CenterNthSelector,
    DirectionMinMaxSelector,
    BinarySelector,
    AndSelector,
    SumSelector,
    SubtractSelector,
    InverseSelector,
    StringSyntaxSelector,
)
from . import exporters
from . import importers
from . import selectors
from . import assembly

__version__ = "2.4.0"
__author__ = "CadQuery Contributors"
__license__ = "Apache License 2.0"
__url__ = "https://github.com/CadQuery/cadquery"

# Personal fork: https://github.com/myusername/cadquery
# Studying CadQuery internals for generative design experiments.

__all__ = [
    # Core workplane
    "Workplane",
    "CQContext",
    # Geometry primitives
    "Vector",
    "Matrix",
    "Plane",
    "BoundBox",
    # Shape types
    "Shape",
    "Vertex",
    "Edge",
    "Wire",
    "Face",
    "Shell",
    "Solid",
    "Compound",
    "CompSolid",
    # Assembly
    "Assembly",
    "ConstraintKind",
    # Selectors
    "NearestToPointSelector",
    "ParallelDirSelector",
    "DirectionSelector",
    "PerpendicularDirSelector",
    "TypeSelector",
    "RadiusNthSelector",
    "CenterNthSelector",
    "DirectionMinMaxSelector",
    "BinarySelector",
    "AndSelector",
    "SumSelector",
    "SubtractSelector",
    "InverseSelector",
    "StringSyntaxSelector",
    # Modules
    "exporters",
    "importers",
    "selectors",
    "assembly",
]
