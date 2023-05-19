
from source.questions.commontools.Answer_choices import AnswerChoices


class SolidPrinciples:
    def __init__(self):
        self.__name = "SOLID Principles"
        self.__description = """SOLID Principles are the five design principles of object-oriented programming and design.
         They are a mnemonic acronym, giving acronyms to each of the principles: Single responsibility,  
         Open–closed, Liskov substitution, Interface segregation, and Dependency inversion. The principles are a subset
         of many principles promoted by American software engineer and instructor Robert C. Martin. They are intended to 
         make software designs more understandable, flexible and maintainable."""
        self.tipsToAnswer = """Read the description in the following file : Question2.pynb and choose the correct 
        answer from AnswerChoices enum. Then implement each method of this class."""

    def get_answer_for_problem_A(self):
        return AnswerChoices.B 
    
    def get_answer_for_problem_B(self):
        return AnswerChoices.D
    
    def get_answer_for_problem_C(self):
        return AnswerChoices.C

    def get_answer_for_problem_D(self):
        return AnswerChoices.A

    def get_answer_for_problem_E(self):
        return AnswerChoices.E
