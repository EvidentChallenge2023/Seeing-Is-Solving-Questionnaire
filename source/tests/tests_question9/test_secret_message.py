import unittest

# from source.questions.question9.Secret_message import SecretMessage
from source.tests.tests_question9.Secret_message import SecretMessage


class TestQuestion9(unittest.TestCase):

    def setUp(self):
        self.secret_massage = SecretMessage()
        self.answer = "« Solve with vision »"

    def test_secret_message(self):
        self.assertEqual(self.secret_massage.get_secret_message(), self.answer)
