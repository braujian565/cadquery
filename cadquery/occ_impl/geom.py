"""Geometry primitives and transformations for CadQuery.

This module provides core geometric types including vectors, matrices,
planes, and bounding boxes used throughout the CadQuery framework.
"""

from typing import Optional, Tuple, Union, overload
import math

from OCC.Core.gp import (
    gp_Vec,
    gp_Pnt,
    gp_Dir,
    gp_Ax1,
    gp_Ax2,
    gp_Ax3,
    gp_Trsf,
    gp_GTrsf,
    gp_XYZ,
)
from OCC.Core.Bnd import Bnd_Box
from OCC.Core.BRepBndLib import brepbndlib_Add


class Vector:
    """A 3D vector with support for common geometric operations.

    Wraps the OCC gp_Vec type and provides a more Pythonic interface.
    """

    def __init__(self, *args):
        """Create a Vector from various input formats.

        Accepts:
            - Vector(x, y, z): three floats
            - Vector((x, y, z)): a tuple or list
            - Vector(gp_Vec): an OCC gp_Vec object
            - Vector(gp_Pnt): an OCC gp_Pnt object
        """
        if len(args) == 3:
            self._v = gp_Vec(*[float(a) for a in args])
        elif len(args) == 1:
            arg = args[0]
            if isinstance(arg, (tuple, list)):
                self._v = gp_Vec(float(arg[0]), float(arg[1]), float(arg[2]))
            elif isinstance(arg, gp_Vec):
                self._v = arg
            elif isinstance(arg, gp_Pnt):
                self._v = gp_Vec(arg.X(), arg.Y(), arg.Z())
            elif isinstance(arg, gp_Dir):
                self._v = gp_Vec(arg)
            else:
                raise TypeError(f"Cannot create Vector from {type(arg)}")
        else:
            raise TypeError(f"Expected 1 or 3 arguments, got {len(args)}")

    @property
    def x(self) -> float:
        return self._v.X()

    @property
    def y(self) -> float:
        return self._v.Y()

    @property
    def z(self) -> float:
        return self._v.Z()

    def length(self) -> float:
        """Return the magnitude of the vector."""
        return self._v.Magnitude()

    def normalized(self) -> "Vector":
        """Return a unit vector in the same direction."""
        mag = self.length()
        if mag < 1e-10:
            raise ValueError("Cannot normalize a zero-length vector")
        return Vector(self.x / mag, self.y / mag, self.z / mag)

    def dot(self, other: "Vector") -> float:
        """Compute the dot product with another vector."""
        return self._v.Dot(other._v)

    def cross(self, other: "Vector") -> "Vector":
        """Compute the cross product with another vector."""
        return Vector(self._v.Crossed(other._v))

    def add(self, other: "Vector") -> "Vector":
        return Vector(self._v.Added(other._v))

    def sub(self, other: "Vector") -> "Vector":
        return Vector(self._v.Subtracted(other._v))

    def multiply(self, scale: float) -> "Vector":
        return Vector(self._v.Multiplied(scale))

    def angle(self, other: "Vector") -> float:
        """Return the angle in degrees between this vector and another."""
        # math.degrees is cleaner than multiplying by (180 / math.pi) manually
        return math.degrees(self._v.Angle(other._v))
