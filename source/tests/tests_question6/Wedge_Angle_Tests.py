import unittest
# from source.questions.question6.Wedge_angle import WedgeAngle
from source.tests.tests_question6.Wedge_angle import WedgeAngle


class TestQuestion6(unittest.TestCase):

    def setUp(self):
        self.wedge_angle = WedgeAngle()

    def test_wedge_angle(self):
        self.assertAlmostEqual(self.wedge_angle.get_wedge_angle_in_degrees(), 13.5, 1)
    
 
 
