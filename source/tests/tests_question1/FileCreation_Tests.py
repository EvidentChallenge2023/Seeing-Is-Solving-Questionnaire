# import unittest
# import h5py
# import os
# import numpy as np
# from unittest.mock import MagicMock

# # from source.questions.question1.FileCreation import FileCreation
# from source.tests.tests_question1.FileCreationSolution import FileCreationSolution
# from source.questions.commontools.Answer_choices import AnswerChoices


# class FileCreation_Tests(unittest.TestCase):

#     def setUp(self):
#         self.fileCreation = FileCreationSolution()

#     def test_CreateHdf5_ProblemA(self):
#         current_path = os.getcwd()
#         directory = f"{current_path}\\source\\questions\\Question1\\"
#         fileExist = False
#         try:
#             self.fileCreation.CreateHdf5_ProblemA()
#             with h5py.File(directory + 'EvidentChallenge.hdf5', "r") as file:
#                 fileExist = True
#                 self.assertTrue(fileExist)
                
#                 dataset_names = list(file.keys())
#                 self.assertEqual(len(dataset_names), 2, "There should be only 2 datasets in file")
#                 self.assertTrue('RawAScan' in dataset_names, "Dataset RawAscan doesn't exist in file")
#                 self.assertTrue('RawCScan' in dataset_names, "Dataset RawCscan doesn't exist in file")
                
#                 shapeAScan = file['RawAScan'].shape
#                 shapeCScan = file['RawCScan'].shape
                
#                 self.assertEqual(len(shapeAScan), 2)
#                 self.assertEqual(shapeAScan[0], 401)
#                 self.assertEqual(shapeAScan[1], 31)

#                 self.assertEqual(len(shapeCScan), 2)
#                 self.assertEqual(shapeCScan[0], 401)
#                 self.assertEqual(shapeCScan[1], 93)
#         except OSError:
#             self.assertTrue(fileExist, 'Cannot find file EvidentChallenge.h5')
        
#     def test_CreateHdf5_ProblemB(self):
#         current_path = os.getcwd()
#         directory = f"{current_path}\\source\\questions\\Question1\\"
#         fileExist = False
#         try:
#             self.fileCreation.CreateHdf5_ProblemB()
#             with h5py.File(directory + 'EvidentChallengeBin.hdf5', "r") as file:
#                 fileExist = True
#                 self.assertTrue(fileExist)
                
#                 dataset_names = list(file.keys())
#                 self.assertEqual(len(dataset_names), 2, "There should be only 2 datasets in file")
#                 self.assertTrue('RawAScan' in dataset_names, "Dataset RawAscan doesn't exist in file")
#                 self.assertTrue('RawCScan' in dataset_names, "Dataset RawCscan doesn't exist in file")
                
#                 shapeAScan = file['RawAScan'].shape
#                 shapeCScan = file['RawCScan'].shape
                
#                 self.assertEqual(len(shapeAScan), 2)
#                 self.assertEqual(shapeAScan[0], 401)
#                 self.assertEqual(shapeAScan[1], 31)

#                 self.assertEqual(len(shapeCScan), 2)
#                 self.assertEqual(shapeCScan[0], 401)
#                 self.assertEqual(shapeCScan[1], 93)
#         except OSError:
#             self.assertTrue(fileExist, 'Cannot find file EvidentChallengeBin.h5')
    
#     def test_GetAScanValue_ProblemC(self): 
#         list = self.fileCreation.GetAScanValue_ProblemC()
#         self.assertEqual(1, len(list))
#         list[0].replace(" ", "")
#         self.assertEqual(list[0].upper(), '020000006D989937E76DCF38')
    
#     def test_GetCScanValue_ProblemD(self): 
#         ls = self.fileCreation.GetCScanValue_ProblemD()
#         self.assertEqual(3, len(ls))
        
#         correctListInCase = [value.replace(" ", "") for value in ls]
#         correctListInCase = [value.upper() for value in ls]
#         self.assertTrue(np.isin('00000000C814000076928C37A1438D37E94E87370FFD2838', correctListInCase))
#         self.assertTrue(np.isin('0000000099610000BE387A38203D7B389569303897DF8A38', correctListInCase))
#         self.assertTrue(np.isin('00000000C814000076928C37A1438D37E94E87370FFD2838', correctListInCase))

#     def test_MCQ_ProblemE(self):
#         justification = """Les cscans peuvent avoir jusqu'à 3 gates soit les Gate I, les Gate A et les Gate B. 
#         Et les données du RawCscan sont représentées par leur valeur de gate ainsi chaque valeur de cscan a 3 données possibles."""
#         self.assertEqual(self.fileCreation.MCQ_ProblemE(), AnswerChoices.C, justification)

#     def test_MCQ_ProblemF(self):
#         justification = """Ces valeurs proviennent d'une struct en C# appelé RawAScan et RawCScan respectivement. Ces deux structs
#         ont plusieurs champs qui correspond à 12 byte pour le RawAScan et 24 byte pour le RawCScan. Le StructLayout de chaque struct 
#         est de 4 byte par valeur stockée dans la mémoire. Ainsi, on a respectivement 3 champs pour le ascan et 6 champs pour le CScan
#         qui est multiplié par 4 dans la mémoire."""
#         self.assertEqual(self.fileCreation.MCQ_ProblemF(), AnswerChoices.D, justification)
