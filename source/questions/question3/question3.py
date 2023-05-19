"""
Question 3: Implement only the class EntryPointCalculator to compute delays
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


class EntryPointCalculator:
    """Calculates the entry point which is the intersection
    of the incident and refracted rays at the interface.
    TODO: Implement me!
    """
    def __init__(self, point_p, point_q, speed_v1, speed_v2) -> None:
        # To implement
        pass

    def calculate_entry_point(self) -> Point:
        """Calculate the entry point."""
        # To implement
        return Point(float('nan'), float('nan'))


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
    """Represents a line segment that models the ultrasound
    wave propagating in a material at a certain speed."""
    def __init__(self, begin, end, speed) -> None:
        self._begin = begin
        self._end = end
        self._speed = speed

    def get_time_of_flight(self) -> float:
        """Get the time of flight for the ray."""
        return self.__get_length() / self._speed

    def __get_length(self) -> float:
        x_dist = self._end.get_x() - self._begin.get_x()
        y_dist = self._end.get_y() - self._begin.get_y()
        return math.sqrt(x_dist * x_dist + y_dist * y_dist)


class RayPath:
    """Represents the complete path of the ultrasound wave that goes through materials."""
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


class Focusing:
    """Compute the delays for the elements considering the speed in the incident material
    and the speed in the refracted material.
    """
    def __init__(self, elements, incident_speed, refracted_speed) -> None:
        self._elements = elements
        self._incident_speed = incident_speed
        self._refracted_speed = refracted_speed

    def focus_on(self, focal) -> None:
        """Compute the delays for the elements when focusing on a focal point."""
        ray_paths = []
        max_tof = 0.0
        for element in self._elements:
            calc = EntryPointCalculator(element.get_pos(), focal,
                                        self._incident_speed, self._refracted_speed)
            point_o = calc.calculate_entry_point()
            incident_ray = Ray(element.get_pos(), point_o, self._incident_speed)
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


def calculate_delays(elements, rexolite_speed, steel_speed, focal) -> None:
    """Calculate the delays to the focal point and fill the values in the elements passed."""
    focusing = Focusing(elements, rexolite_speed, steel_speed)
    focusing.focus_on(focal)


def validate_delays(elements, expected_delays, tolerance=1e-6) -> None:
    """Validate the delays assigned to each elements with the expected delays."""
    i = 0
    for element in elements:
        print(f"Delay for element {element.get_id()} = {element.get_delay()}")
        assert abs(expected_delays[i] - element.get_delay()) < tolerance
        i += 1


def run_example_validation() -> None:
    """Validate an example with the expected soluton"""
    speed_v1_example = 2330
    speed_v2_example = 5890
    elements_example = Elements([Element(Point(-8, 11)), Element(Point(-7, 12)),
                                 Element(Point(-6, 13)), Element(Point(-5, 14))])
    focal_example = Point(7, -5)
    expected_delays_example = [0.0007662, 0.0005171, 0.0002622, 0.0]

    calculate_delays(elements_example, speed_v1_example, speed_v2_example, focal_example)
    validate_delays(elements_example, expected_delays_example)


def calculate_delays_problem1() -> Elements:
    """Problem 1"""
    speed_v1_problem1 = 2330
    speed_v2_problem1 = 5890
    elements_problem1 = Elements([Element(Point(-8, 11)), Element(Point(-7, 12)),
                                  Element(Point(-6, 13)), Element(Point(-5, 14))])
    focal_problem1 = Point(-19.4, -11)
    calculate_delays(elements_problem1, speed_v1_problem1, speed_v2_problem1, focal_problem1)
    return elements_problem1


def calculate_delays_problem2() -> Elements:
    """Problem 2"""
    speed_v1_problem2 = 2330
    speed_v2_problem2 = 5890
    elements_problem2 = Elements([Element(Point(-8, 11)), Element(Point(-7, 11)),
                                  Element(Point(-6, 11)), Element(Point(-5, 11))])
    focal_problem2 = Point(7.7, -3)
    calculate_delays(elements_problem2, speed_v1_problem2, speed_v2_problem2, focal_problem2)
    return elements_problem2


def calculate_delays_problem3() -> Elements:
    """Problem 3"""
    speed_v1_problem3 = 2330
    speed_v2_problem3 = 2340
    elements_problem3 = Elements([Element(Point(-8, 5)), Element(Point(-7, 5)),
                                  Element(Point(-6, 5)), Element(Point(-5, 5))])
    focal_problem3 = Point(-6.5, -2)
    calculate_delays(elements_problem3, speed_v1_problem3, speed_v2_problem3, focal_problem3)
    return elements_problem3
