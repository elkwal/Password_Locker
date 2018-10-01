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
    def test__init__(self):
        """
		test__init__ to check if the object is instantiated correctly
		"""
        self.assertEqual(self.new_user.first_name, "Sylvia")
        self.assertEqual(self.new_user.last_name, "Elkwal")
        self.assertEqual(self.new_user.password, "Elukwal3")
    def test_save_user(self):
        """
		Test to check if the new users information is saved into the users list
		"""
        self.new_user.save_user()
        self.assertEqual(len(User.users_list), 1)
