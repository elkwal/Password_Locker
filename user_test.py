import unittest
import pyperclip
from user import User,Credential

class TestUser(unittest.TestCase):
    """
	Test class which defines test cases for the user class behaviours
	"""

    def setUp(self):
        """
	    Set up method to run before each test cases.
		"""
        self.new_user = User("Sylvia", "Elkwal", "Elukwal3")
