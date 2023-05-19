# import unittest
# import random
# # from source.questions.question8.question8_2.DataStability import DataStability 
# from source.questions.question8.question8_2.Taille_Instances import TailleInstance
# from source.tests.tests_question8.testquestion8_2.DataStability import DataStability
# import csv


# class TestQuestion8_2(unittest.TestCase):

#     def setUp(self):
#         self.tri_Data_Stability = DataStability(list_to_sort=[])
       
#     def test_simple(self):
#         vecteur = []
#         n = TailleInstance.TEST_SIMPLE.value
#         for i in range(n, 0, -1):
#             second = random.choice(TailleInstance.liste_second_Val.value)
#             vecteur.append((i, second))
        
#         path_of_dataset_test_simple = "source/questions/question8/question8_2/dataset_test_simple.csv"
#         with open(path_of_dataset_test_simple, "w", newline='') as fichier:
#             writer_Of_data = csv.writer(fichier)
#             for data in vecteur:
#                 writer_Of_data.writerow(data)

#         self.tri_Data_Stability.list_to_sort = vecteur
#         copie1 = self.tri_Data_Stability.list_to_sort
#         copie2 = self.tri_Data_Stability.list_to_sort

#         self.tri_Data_Stability.perform_sort()
#         copie2.sort(key=lambda x: x[0])
#         self.assertEqual(copie1, copie2)
    
#     def test_With_Duplicate(self):
#         vecteur = []
#         n = TailleInstance.TEST_DOUBLONS.value

#         for i in range(n):
#             second = random.choice(TailleInstance.liste_second_Val.value)
#             vecteur.append((29 * i % 17, second))
#         path_of_dataset_test_with_duplicate = "source/questions/question8/question8_2/dataset_test_with_duplicate.csv"
#         with open(path_of_dataset_test_with_duplicate, "w", newline="") as fichier:
#             writer_of_data = csv.writer(fichier)
#             for data in vecteur:
#                 writer_of_data.writerow(data)

#         self.tri_Data_Stability.list_to_sort = vecteur
#         copie1 = self.tri_Data_Stability.list_to_sort
#         copie2 = self.tri_Data_Stability.list_to_sort

#         self.tri_Data_Stability.perform_sort()
#         copie2.sort(key=lambda x: x[0])

#         self.assertEqual(copie1, copie2)
    
#     def test_degenerate(self):
#         vecteur = []
#         n = TailleInstance.TEST_DEGENERER.value
#         for i in range(n):
#             second = random.choice(TailleInstance.liste_second_Val.value)
#             vecteur.append((2 + i % 7, second))
#         path_of_dataset_test_with_degenerate = "source/questions/question8/question8_2/dataset_test_degenerate.csv"
#         with open(path_of_dataset_test_with_degenerate, "w", newline="") as fichier:
#             writer_of_data = csv.writer(fichier)
#             for data in vecteur:
#                 writer_of_data.writerow(data)

#         self.tri_Data_Stability.list_to_sort = vecteur
#         copie1 = self.tri_Data_Stability.list_to_sort
#         copie2 = self.tri_Data_Stability.list_to_sort
#         self.tri_Data_Stability.perform_sort()
#         copie2.sort(key=lambda x: x[0])
#         self.assertEqual(copie1, copie2)
    
#     def test_random(self):
#         random.seed(TailleInstance.GERME.value)
#         n = TailleInstance.TEST_RANDOM.value
#         nb_instance = TailleInstance.NB_INSTANCE.value
#         for sim in range(nb_instance):
#             vecteur = []
#             for i in range(n):
#                 second = random.choice(TailleInstance.liste_second_Val.value)
#                 vecteur.append((random.randint(1, 999), second))
#         path_of_dataset_test_random = "source/questions/question8/question8_2/dataset_test_random.csv"
#         with open(path_of_dataset_test_random, "w", newline="") as fichier:
#             writer_of_data = csv.writer(fichier)
#             for data in vecteur:
#                 writer_of_data.writerow(data)

#         self.tri_Data_Stability.list_to_sort = vecteur
#         copie1 = self.tri_Data_Stability.list_to_sort
#         copie2 = self.tri_Data_Stability.list_to_sort

#         self.tri_Data_Stability.perform_sort()
#         copie2.sort(key=lambda x: x[0])
#         self.assertEqual(copie1, copie2)
