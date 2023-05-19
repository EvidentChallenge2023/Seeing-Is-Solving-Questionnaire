"""
Test suite for Question 3 solution
"""
import math
from source.tests.tests_question3.question3_solution import Point, Element, Elements
from source.tests.tests_question3.question3_solution import Ray, RayPath
from source.tests.tests_question3.question3_solution import EntryPointCalculator, Focusing


class TestQuestion3Solution:
    """Test Question 3 solution"""

    def test_that_point_creation_gives_correct_coordinates(self):
        expected_x = 42.0
        expected_y = -32.2
        point = Point(42.0, -32.2)
        assert expected_x == point.get_x()
        assert expected_y == point.get_y()

    def test_that_element_creation_gives_correct_values(self):
        expected_point = Point(42.0, -32.2)
        element = Element(expected_point)
        self.__validate_point(expected_point, element.get_pos())
        assert math.isnan(element.get_delay())
        assert 0 == element.get_id()

    def test_that_elements_creation_gives_correct_values(self):
        e_0 = Element(Point(42.0, -2.718))
        e_1 = Element(Point(2.0, 8.98))
        e_2 = Element(Point(-6.7, 4.2))
        e_3 = Element(Point(-8.9, -2.2))
        element_list = [e_0, e_1, e_2, e_3]
        i = 0
        elements = Elements(element_list)
        for element in elements:
            self.__validate_point(element_list[i].get_pos(), element.get_pos())
            i += 1

    def test_that_ray_gets_correct_time_of_flight(self):
        ray = Ray(Point(0.0, 0.0), Point(10.0, 0.0), 5.0)
        assert 2.0 == ray.get_time_of_flight()

    def test_that_rays_gets_correct_time_of_flight(self):
        ray_0 = Ray(Point(0.0, 0.0), Point(10.0, 0.0), 5.0)
        ray_1 = Ray(Point(10.0, 0), Point(10.0, 12.0), 3.0)
        emitter = Element(Point(0.0, 0.0))
        ray_path = RayPath(emitter, [ray_0, ray_1])
        assert 6.0 == ray_path.get_time_of_flight()

    def test_that_entry_point_is_valid(self):
        point_p = Point(-8, 11)
        point_q = Point(7, -5)
        incident_speed = 2330
        refracted_speed = 5890

        calc = EntryPointCalculator(
            point_p, point_q, incident_speed, refracted_speed)
        entry_point = calc.calculate_entry_point()
        expected_point = Point(-3.7714763857600335, 0)
        self.__validate_point(expected_point, entry_point)

    def test_that_delays_are_correct(self):
        elements = self.__get_elements()
        incident_speed = 2330
        refracted_speed = 5890
        focal_point = Point(5.0, -7.0)
        focusing = Focusing(elements, incident_speed, refracted_speed)
        focusing.focus_on(focal_point)
        self.__validate_delays(elements)

    def test_solutionned_example(self):
        speed_v1 = 2330
        speed_v2 = 5890
        expected_delays = [0.0007661608557311128,
                           0.0005171024816518583, 0.0002622390039994753, 0.0]
        focal = Point(7, -5)
        elements = Elements([Element(Point(-8, 11)), Element(Point(-7, 12)),
                            Element(Point(-6, 13)), Element(Point(-5, 14))])
        focusing = Focusing(elements, speed_v1, speed_v2)
        focusing.focus_on(focal)
        self.__print_delay(elements)
        self.__validate_delays_relative_tolerance(elements, expected_delays)

    def test_problem1(self):
        speed_v1_problem1 = 2330
        speed_v2_problem1 = 5890
        elements_problem1 = Elements([Element(Point(-8, 11)),
                                      Element(Point(-7, 12)),
                                      Element(Point(-6, 13)),
                                      Element(Point(-5, 14))])
        focal_problem1 = Point(-19.4, -11)
        expected_delays = [0.001964652721658822,
                           0.0013181596252849447, 0.0006628689557412557, 0.0]
        focusing = Focusing(elements_problem1,
                            speed_v1_problem1, speed_v2_problem1)
        focusing.focus_on(focal_problem1)
        self.__print_delay(elements_problem1)
        self.__validate_delays_relative_tolerance(
            elements_problem1, expected_delays)

    def test_problem2(self):
        speed_v1_problem2 = 2330
        speed_v2_problem2 = 5890
        elements_problem2 = Elements([Element(Point(-8, 11)),
                                      Element(Point(-7, 11)),
                                      Element(Point(-6, 11)),
                                      Element(Point(-5, 11))])
        focal_problem2 = Point(7.7, -3)
        expected_delays = [0.0,
                           0.00016343055038509947,
                           0.00032562830306877115,
                           0.00048623023199616776]
        focusing = Focusing(elements_problem2,
                            speed_v1_problem2, speed_v2_problem2)
        focusing.focus_on(focal_problem2)
        self.__print_delay(elements_problem2)
        self.__validate_delays_relative_tolerance(
            elements_problem2, expected_delays)

    def test_problem3(self):
        speed_v1_problem3 = 2330
        speed_v2_problem3 = 2340
        elements_problem3 = Elements([Element(Point(-8, 5)),
                                      Element(Point(-7, 5)),
                                      Element(Point(-6, 5)),
                                      Element(Point(-5, 5))])
        focal_problem3 = Point(-6.5, -2)
        expected_delays = [0.0005174656484054287,
                           0.0005779391703512314, 0.0005050181853061809, 0.0]
        focusing = Focusing(elements_problem3,
                            speed_v1_problem3, speed_v2_problem3)
        focusing.focus_on(focal_problem3)
        self.__print_delay(elements_problem3)
        self.__validate_delays_relative_tolerance(
            elements_problem3, expected_delays)
        
    def test_problem3_benchmark_solution(self, benchmark):
        incident_speed = 2330
        refracted_speed = 2340
        focal_point = Point(-6.5, -2)
        elements = Elements([Element(Point(-8, 5)), Element(Point(-7, 5)),
                             Element(Point(-6, 5)), Element(Point(-5, 5))])
        focusing = Focusing(elements, incident_speed, refracted_speed)
        benchmark(focusing.focus_on, focal_point)

    def test_real_example(self):
        speed_v1 = 2330
        speed_v2 = 5890
        e_0 = Element(Point(-0.020809999999999999, 0.0065700000000000003))
        e_1 = Element(Point(-0.020295699619578732, 0.0068790228449460327))
        e_2 = Element(Point(-0.019781399239157463, 0.0071880456898920650))
        e_3 = Element(Point(-0.019267098858736197, 0.0074970685348380982))
        e_4 = Element(Point(-0.018752798478314930, 0.0078060913797841306))
        e_5 = Element(Point(-0.018238498097893661, 0.0081151142247301630))
        e_6 = Element(Point(-0.017724197717472395, 0.0084241370696761953))
        e_7 = Element(Point(-0.017209897337051128, 0.0087331599146222277))
        e_8 = Element(Point(-0.016695596956629859, 0.0090421827595682600))
        e_9 = Element(Point(-0.016181296576208593, 0.0093512056045142924))
        elements = Elements([e_0, e_1, e_2, e_3, e_4, e_5, e_6, e_7, e_8, e_9])
        focal = Point(-0.0061779648334810231, -0.01)
        expected_delays = [5.9383468801321856E-07,
                           5.3512711575154054E-07,
                           4.7485990339267031E-07,
                           4.1292627545601418E-07,
                           3.4921575259215094E-07,
                           2.8361496244477105E-07,
                           2.1600862272911184E-07,
                           1.4628069374231419E-07,
                           7.431567309922723E-08,
                           0]
        focusing = Focusing(elements, speed_v1, speed_v2)
        focusing.focus_on(focal)
        self.__print_delay(elements)
        self.__validate_delays_relative_tolerance(elements, expected_delays)

    def __validate_point(self, expected_point, actual_point):
        assert expected_point.get_x() == actual_point.get_x()
        assert expected_point.get_y() == actual_point.get_y()

    def __get_elements(self):
        e_0 = Element(Point(-10.0, 11.0))
        e_1 = Element(Point(-9.0, 12.0))
        e_2 = Element(Point(-8.0, 13.0))
        e_3 = Element(Point(-7.0, 14.0))
        e_4 = Element(Point(-6.0, 15.0))
        e_5 = Element(Point(-7.0, 16.0))
        e_6 = Element(Point(-4.0, 17.0))
        e_7 = Element(Point(-3.0, 18.0))
        e_8 = Element(Point(-2.0, 19.0))
        e_9 = Element(Point(-1.0, 20.0))
        elements = Elements([e_0, e_1, e_2, e_3, e_4, e_5, e_6, e_7, e_8, e_9])
        return elements

    def __validate_delays(self, elements):
        expected_delays = [
            0.002735626122917629, 0.0024715292715448787,
            0.002200152309880179, 0.001920214922428852,
            0.001630426847754027, 0.0010984127590599434,
            0.001016710075718513, 0.0006910522778982749,
            0.000352192677024550, 0.0
        ]
        self.__validate_delays_relative_tolerance(elements, expected_delays)

    def __validate_delays_relative_tolerance(self, elements, expected_delays):
        i = 0
        for element in elements:
            actual_delay = element.get_delay()
            assert math.fabs(expected_delays[i] - actual_delay) < 1e-6
            i += 1

    def __print_delay(self, elements):
        for element in elements:
            print(element.get_delay())
