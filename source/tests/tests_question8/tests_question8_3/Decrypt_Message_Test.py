import unittest
# from source.questions.question8.question8_3.question8_3 import Decoder
from question8_3 import Decoder


class TestQuestion8_3(unittest.TestCase):
    def setUp(self):
        # The sun is the key
        self.decoder = Decoder()
        self.decrypted_message = "Videre est solvere"
    
    def test_question8_2(self):
        self.assertEqual(self.decoder.decrypt(), self.decrypted_message)
        
