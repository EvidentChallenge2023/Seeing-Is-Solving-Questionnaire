import unittest
from unittest.mock import MagicMock
from source.tests.tests_question8.testquestion8_1.ResponseQuestion8_1 import ReponseQuestion8_1
from source.tests.tests_question8.testquestion8_1.Decryptor import Decryptor
from source.questions.question8.question8_1.MessagesToDecript import MessagesToDecript


class TestQuestion8(unittest.TestCase):
    def setUp(self):
        self.test_decrypt_data = Decryptor(" ")
    
    def test_question8_1_A(self):
        self.test_decrypt_data.data = MessagesToDecript.ENCODED_STRING_A.value
        self.assertEqual(self.test_decrypt_data.decrypt_data(), ReponseQuestion8_1.DATA_DECRYPTED_A.value)
    
    def test_question8_1_B(self):
        self.test_decrypt_data.data = MessagesToDecript.ENCODED_STRING_B.value
        self.assertEqual(self.test_decrypt_data.decrypt_data(), ReponseQuestion8_1.DATA_DECRYPTED_B.value)
        
    def test_question8_1_C(self):
        self.test_decrypt_data.data = MessagesToDecript.ENCODED_STRING_C.value
        self.assertEqual(self.test_decrypt_data.decrypt_data(), ReponseQuestion8_1.DATA_DECRYPTED_C.value)
       
    def test_question8_1_D(self):
        self.test_decrypt_data.data = MessagesToDecript.ENCODED_STRING_D.value
        self.assertEqual(self.test_decrypt_data.decrypt_data(), ReponseQuestion8_1.DATA_DECRYPTED_D.value)

    def test_question8_1_E(self):
        self.test_decrypt_data.data = MessagesToDecript.ENCODED_STRING_E.value
        self.assertEqual(self.test_decrypt_data.decrypt_data(), ReponseQuestion8_1.DATA_DECRYPTED_E.value)
