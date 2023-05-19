import unittest

from source.questions.commontools.Answer_choices import AnswerChoices
from source.tests.tests_question4.Design_patterns import DesignPatterns
# from source.questions.question4.Design_patterns import DesignPatterns


class TestQuestion4(unittest.TestCase):

    def setUp(self):
        self.design_patterns = DesignPatterns()

    def test_problem_A(self):
        self.assertEqual(self.design_patterns.get_answer_for_problem_A(), AnswerChoices.Q)
    
    def test_problem_B(self):
        self.assertEqual(self.design_patterns.get_answer_for_problem_B(), AnswerChoices.K)
    
    def test_problem_C(self):
        self.assertEqual(self.design_patterns.get_answer_for_problem_C(), AnswerChoices.D)
    
    def test_problem_D(self):
        self.assertEqual(self.design_patterns.get_answer_for_problem_D(), AnswerChoices.T)
    
    def test_problem_E(self):
        self.assertEqual(self.design_patterns.get_answer_for_problem_E(), AnswerChoices.L)
 
 
