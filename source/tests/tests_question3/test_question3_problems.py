"""
Test suite for Question 3 probles
"""
from source.questions.question3.question3 import Point, Element, Elements
from source.questions.question3.question3 import Focusing


class TestQuestion3Problems:
    """Test Question 3 problems"""

    is_correction = False

    def test_problem1(self):
        if TestQuestion3Problems.is_correction:
            actual_elements = self.__calculate_delays_problem1()
            expected_delays = [0.001964652721658822,
                               0.0013181596252849447, 0.0006628689557412557, 0.0]
            self.__validate_delays(actual_elements, expected_delays)
        else:
            assert True

    def test_problem2(self):
        if TestQuestion3Problems.is_correction:
            actual_elements = self.__calculate_delays_problem2()
            expected_delays = [0.0,
                               0.00016343055038509947,
                               0.00032562830306877115,
                               0.00048623023199616776]
            self.__validate_delays(actual_elements, expected_delays)
        else:
            assert True

    def test_problem3(self):
        if TestQuestion3Problems.is_correction:
            actual_elements = self.__calculate_delays_problem3()
            expected_delays = [0.0005174656484054287,
                               0.0005779391703512314, 0.0005050181853061809, 0.0]
            self.__validate_delays(actual_elements, expected_delays)
        else:
            assert True

    def test_problem3_benchmark(self, benchmark):
        if TestQuestion3Problems.is_correction:
            incident_speed = 2330
            refracted_speed = 2340
            focal_point = Point(-6.5, -2)
            elements = Elements([Element(Point(-8, 5)), Element(Point(-7, 5)),
                                Element(Point(-6, 5)), Element(Point(-5, 5))])
            focusing = Focusing(elements, incident_speed, refracted_speed)
            benchmark(focusing.focus_on, focal_point)
        else:
            assert True

    def __calculate_delays(self, elements, rexolite_speed, steel_speed, focal) -> None:
        """Calculate the delays to the focal point and fill the values in the elements passed."""
        focusing = Focusing(elements, rexolite_speed, steel_speed)
        focusing.focus_on(focal)

    def __validate_delays(self, elements, expected_delays, tolerance=1e-6) -> None:
        """Validate the delays assigned to each elements with the expected delays."""
        i = 0
        for element in elements:
            print(f"Delay for element {element.get_id()} = {element.get_delay()}")
            assert abs(expected_delays[i] - element.get_delay()) < tolerance
            i += 1

    def __calculate_delays_problem1(self) -> Elements:
        """Problem 1"""
        speed_v1_problem1 = 2330
        speed_v2_problem1 = 5890
        elements_problem1 = Elements([Element(Point(-8, 11)), Element(Point(-7, 12)),
                                      Element(Point(-6, 13)), Element(Point(-5, 14))])
        focal_problem1 = Point(-19.4, -11)
        self.__calculate_delays(elements_problem1, speed_v1_problem1,
                                speed_v2_problem1, focal_problem1)
        return elements_problem1

    def __calculate_delays_problem2(self) -> Elements:
        """Problem 2"""
        speed_v1_problem2 = 2330
        speed_v2_problem2 = 5890
        elements_problem2 = Elements([Element(Point(-8, 11)), Element(Point(-7, 11)),
                                      Element(Point(-6, 11)), Element(Point(-5, 11))])
        focal_problem2 = Point(7.7, -3)
        self.__calculate_delays(elements_problem2, speed_v1_problem2,
                                speed_v2_problem2, focal_problem2)
        return elements_problem2

    def __calculate_delays_problem3(self) -> Elements:
        """Problem 3"""
        speed_v1_problem3 = 2330
        speed_v2_problem3 = 2340
        elements_problem3 = Elements([Element(Point(-8, 5)), Element(Point(-7, 5)),
                                      Element(Point(-6, 5)), Element(Point(-5, 5))])
        focal_problem3 = Point(-6.5, -2)
        self.__calculate_delays(elements_problem3, speed_v1_problem3,
                                speed_v2_problem3, focal_problem3)
        return elements_problem3
