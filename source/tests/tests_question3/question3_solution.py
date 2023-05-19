"""
Compute delays for the generation of ultrasound waves.
"""
import math
from typing import Iterator


class Point:
    """Represents a point in 2 dimensions."""

    def __init__(self, x_coord, y_coord) -> None:
        self._x_coord = x_coord
        self._y_coord = y_coord

    def get_x(self) -> float:
        """Get X point coordinate."""
        return self._x_coord

    def get_y(self) -> float:
        """Get Y point coordinate."""
        return self._y_coord


class Element:
    """A transducer element."""

    def __init__(self, pos) -> None:
        self._pos = pos
        self._delay = float('nan')
        self._id = 0

    def assign_delay(self, delay) -> None:
        """Assign an electronic delay to the element."""
        self._delay = delay

    def get_pos(self) -> Point:
        """Get the position of the element on the transducer."""
        return self._pos

    def get_delay(self) -> float:
        """Get the electronic delay."""
        return self._delay

    def assign_id(self, ident) -> None:
        """Assign an identifier to the element."""
        self._id = ident

    def get_id(self) -> int:
        """Get the identifier of the element."""
        return self._id


class Elements:
    """Collection of element."""

    def __init__(self, elements) -> None:
        self._elements = elements
        ident = 0
        for element in self._elements:
            element.assign_id(ident)
            ident += 1

    def __iter__(self) -> Iterator[Element]:
        for element in self._elements:
            yield element


class Ray:
    """Represent a segment of the ultrasound beam propagating in a material
      at a certain speed."""

    def __init__(self, begin, end, speed) -> None:
        self._begin = begin
        self._end = end
        self._speed = speed

    def get_time_of_flight(self) -> float:
        """Get the time of flight for the ray."""
        return self.__get_length() / self._speed

    def __get_length(self):
        x_dist = self._end.get_x() - self._begin.get_x()
        y_dist = self._end.get_y() - self._begin.get_y()
        return math.sqrt(x_dist * x_dist + y_dist * y_dist)


class RayPath:
    """Path of the ultrasound beam that goes through materials."""

    def __init__(self, emitter, rays) -> None:
        self._emitter = emitter
        self._rays = rays

    def __iter__(self) -> Iterator[Ray]:
        for ray in self._rays:
            yield ray

    def get_time_of_flight(self) -> float:
        """Get total time of flight for all the rays of the path."""
        total = 0.0
        for ray in self._rays:
            total += ray.get_time_of_flight()
        return total

    def get_emitter(self) -> Element:
        """Get the emitter that has emit the first ray."""
        return self._emitter


class EntryPointCalculator:
    """Calculates the entry point which is the intersection
    of the incident and refracted rays at the interface.
    """

    def __init__(self, point_p, point_q, speed_v1, speed_v2) -> None:
        self._p = point_p
        self._q = point_q
        self._v = speed_v1
        self._w = speed_v2
        self._l = abs(self._q.get_x() - self._p.get_x())
        self._a = abs(self._p.get_y())
        self._b = abs(self._q.get_y())
        self._x0 = self._l / 2.0
        self._speed_ratio = self._v / self._w
        self._precision = 1e-9
        self._max_number_iteration = 200

    def evaluate_sinus_incident_angle(self, x_val):
        """Evaluate the sinus of the incident angle."""
        return x_val / math.sqrt(x_val * x_val + self._a * self._a)

    def evaluate_sinus_refracted_angle(self, x_val):
        """Evaluate the sinus of the refracted angle angle."""
        lmx = self._l - x_val
        return lmx / math.sqrt(lmx * lmx + self._b * self._b)

    def calculate_entry_point(self) -> Point:
        """Calculate the entry point."""
        x_val = self._x0
        for _ in range(self._max_number_iteration):
            func = self.__evaluate_least_time_derivation
            func_deriv = self.__evaluate_least_time_second_derivation
            x_val = self.__evaluate_newtons_method_approximation(
                x_val, func, func_deriv)
            sin_t1 = self.evaluate_sinus_incident_angle(x_val)
            sin_t2 = self.evaluate_sinus_refracted_angle(x_val)
            if abs((sin_t1 / sin_t2) - self._speed_ratio) < self._precision:
                return self.__get_entry_point(x_val)
        return self.__get_entry_point(x_val)

    def evaluate_least_time_derivation(self, x_val):
        """Evaluate the least time derivation."""
        return self.__evaluate_least_time_derivation(x_val)

    def evaluate_linear_approximation(self, x_val):
        """Evaluate the linear approximation."""
        bsq = self._b * self._b
        bsqplsq = bsq + self._l * self._l
        slope = 1.0 / (self._a * self._v) + bsq / \
            (self._v * math.sqrt(bsqplsq * bsqplsq * bsqplsq))
        ordinate = self._l / (self._w * math.sqrt(bsqplsq))
        return slope * x_val - ordinate

    def __get_entry_point(self, x_sol) -> Point:
        """Calculate the entry point.
        """
        o_x = self._p.get_x() + x_sol
        o_y = self._p.get_y() - self._a
        return Point(o_x, o_y)

    def __evaluate_least_time_derivation(self, x_val):
        i = x_val / (self._v * math.sqrt(x_val * x_val + self._a * self._a))
        lmx = self._l - x_val
        r_denom = self._w * math.sqrt(lmx * lmx + self._b * self._b)
        return i - lmx / r_denom

    def __evaluate_least_time_second_derivation(self, x_val):
        asq = self._a * self._a
        xsq = x_val * x_val
        i = asq / (self._v * math.sqrt((asq + xsq) *
                   (asq + xsq) * (asq + xsq)))
        bsq = self._b * self._b
        lmxsq = (self._l - x_val) * (self._l - x_val)
        r_val = bsq / (self._w * math.sqrt((bsq + lmxsq) *
                                           (bsq + lmxsq) * (bsq + lmxsq)))
        return i + r_val

    @staticmethod
    def __evaluate_newtons_method_approximation(x_sol, func, func_deriv):
        return x_sol - func(x_sol) / func_deriv(x_sol)


class Focusing:
    """Compute the delays for the elements considering
    the speed in the incident material and the speed in the refracted material.
    """

    def __init__(self, elements, incident_speed, refracted_speed) -> None:
        self._elements = elements
        self._incident_speed = incident_speed
        self._refracted_speed = refracted_speed

    def focus_on(self, focal) -> None:
        """Compute the delays for the elements
        when focusing on a focal point."""
        ray_paths = []
        max_tof = 0.0
        for element in self._elements:
            calc = EntryPointCalculator(element.get_pos(),
                                        focal,
                                        self._incident_speed,
                                        self._refracted_speed)
            point_o = calc.calculate_entry_point()
            incident_ray = Ray(element.get_pos(),
                               point_o, self._incident_speed)
            refracted_ray = Ray(point_o, focal, self._refracted_speed)
            path = RayPath(element, [incident_ray, refracted_ray])
            if max_tof < path.get_time_of_flight():
                max_tof = path.get_time_of_flight()
            ray_paths.append(path)

        for path in ray_paths:
            tof = path.get_time_of_flight()
            delay = max_tof - tof
            emitter = path.get_emitter()
            emitter.assign_delay(delay)
