import unittest

from source.questions.commontools.Answer_choices import AnswerChoices
# from source.questions.question2.Solid_principles import SolidPrinciples
from source.tests.tests_question2.Solid_principles import SolidPrinciples


class TestQuestion2(unittest.TestCase):

    def setUp(self):
        self.solid_principles = SolidPrinciples()

    def test_problem_A(self):
        justification = """The Interface Segregation Principle (ISP) indicates that a class should implement an interface that
          is 100% necessary into that class. Dual probe should not implement an interface with methods or property that 
         it doesn't need. The SetPulserPolarity method is not used by the DualProbe so DualProbe should not implement the
         IProbe interface. A dedicated interface can be created for the PhasedArrayProbe and the IProbe interface could 
         contain only necessary methods and properties for all probe implementations. """
        self.assertEqual(self.solid_principles.get_answer_for_problem_A(), AnswerChoices.B, justification)
    
    def test_problem_B(self):
        justification = """The Open–Closed principle (OCP) states that software entities (classes, modules, functions, etc.) should 
        be open for extension, but closed for modification. In that question, the Renderer class has a method named RenderSignal 
        that has to validate each type of PulserPolarity. If a new type of PulserPolarity is added, the method would have to be 
        modified, violating the Closed portion of the OCP. A dedicated implementation of the method RenderSignal for each type
        of PulserPolarity would be a solution that respects the OCP. """
        self.assertEqual(self.solid_principles.get_answer_for_problem_B(), AnswerChoices.D, justification)
    
    def test_problem_C(self):
        justification = """The Depedency Inversion Principle (DIP) states that high-level modules should depend on abstractions 
        rather than concrete implementations. In that question, the phased array probe is created into the scanner 
        constructor and cannot be mocked into a unit test. The scanner should have an IProbe injected instead of creating
        the probe itself. Even if the probe is exposed into a public property, it is a readonly property that cannot be 
        mocked in C#."""
        self.assertEqual(self.solid_principles.get_answer_for_problem_C(), AnswerChoices.C, justification)
    
    def test_problem_D(self):
        justification = """Liscov Substitution Principle (LSP) states that objects in a program should not inherit from a class
        if they cannot be a substitute of that class without modifying its behavior. In that question, the DualProbe class 
        inherits from the PhasedArrayProbe class but the DualProbe class does not have the same behavior as the PhasedArrayProbe
        class. In many lines of that question, the DualProbe class overrides the behavior of the PhasedArrayProbe class. That 
        violates the LSP.
        """
        self.assertEqual(self.solid_principles.get_answer_for_problem_D(), AnswerChoices.A, justification)
    
    def test_problem_E(self):
        justification = """The Single Responsibility Principle (SRP) is a computer programming principle that states that 
        a module should be responsible to one, and only one, actor. The term actor refers to a group (consisting of one
        or more stakeholders or users) that requires a change in the module. In that case, 3 different groups of people 
        can ask for change in that class. The rendering, the file nanagement and the settings of the probe should all be
        separated into different classes.
        """
        self.assertEqual(self.solid_principles.get_answer_for_problem_E(), AnswerChoices.E, justification)
 
 
