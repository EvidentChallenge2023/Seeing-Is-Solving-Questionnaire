
import h5py
import os
import numpy as np

from source.questions.commontools.Answer_choices import AnswerChoices


class FileCreation: 
    def __init__(self):
        self.__name = "HDF5 questions"
        self.__description = """HDF5 is a weld used file type use over the world in various industry to analyse
        and view data."""
        self.tipsToAnswer = """Read the description in the following file : Question1.pynb. 
        Then implement each method of this class."""
    
    def CreateHdf5_ProblemA(self):
        # Answer problem A here 
        filename = "EvidentChallenge.hdf5"

    def CreateHdf5_ProblemB(self):
        # Answer problem B here 
        filename = "EvidentChallengeBin.hdf5"
    
    def GetAScanValue_ProblemC(self):
        Q3List = []
        # Answer problem C here 
        return Q3List
    
    def GetCScanValue_ProblemD(self):
        Q4List = []
        # Answer problem D here 
        return Q4List
    
    def MCQ_ProblemE(self):
        # Answer problem E here 
        return AnswerChoices.Z
    
    def MCQ_ProblemF(self):
        # Answer problem F here 
        return AnswerChoices.Z
