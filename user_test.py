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
class TestCredentials(unittest.TestCase):
    """
	Test class that defines test cases for the credentials class behaviours.
	"""

    def test_check_existing_user(self):
        """
	    Tests wether the login funtion works well
		"""
        self.new_user = User("Sylvia", "Elkwal", "Elukwal3")
        self.new_user.save_user()
        user2 = User("Caroline", "Mumo", "20172018")
        user2.save_user()

        for user in User.users_list:
            if user.first_name == user2.first_name and user.password == user2.password:
                current_user = user.first_name
        return current_user

        self.assertEqual(current_user, Credential.check_existing_user(user2.password, user2.first_name))

    def setUp(self):
        """
		Function to create an account's credentials before each test
		"""
        self.new_credential = Credential('Sylvia', 'Elkwal', 'Sylvia Elkwal', 'Elukwal3')

    def test__init__(self):
        '''
	    Test to check if intialization was properly done
		'''
        self.assertEqual(self.new_credential.user_name, 'Sylvia')
        self.assertEqual(self.new_credential.site_name, 'Elkwal')
        self.assertEqual(self.new_credential.account_name, 'Sylvia Elkwal')
        self.assertEqual(self.new_credential.password, 'Elukwal3')

    def test_save_credentials(self):
        """
		Test to check if the new credential information is saved in the credentials list
		"""
        self.new_credential.save_credentials()
        Instagram = Credential('Elkwal', 'Instagram', 'Elkwal_Simple', 'Elukwal3')
        Instagram.save_credentials()
        self.assertEqual(len(Credential.credentials_list),2)

    def tearDown(self):
        """
		Function to clear the credentials list after every test
		"""
        User.users_list = []
        Credential.credentials_list = []
    def test_display_credentials(self):
        """
		Test to check if the display_credentials method, displays the correct credentials.
		"""
        self.new_credential.save_credentials()
        Instagram = Credential('Elkwal', 'Instagram', 'Elkwal_Simple', 'Elukwal3')
        Instagram.save_credentials()
        facebook = Credential('Elkwal', 'Facebook', 'Elkwal_Simple', 'Elukwal3')
        facebook.save_credentials()
        self.assertEqual(len(Credential.display_credentials(Instagram.user_name)), 2)

    def test_find_by_site_name(self):
        """
		Test to check if the find_by_site_name method returns the correct credential
		"""
        self.new_credential.save_credentials()
        Instagram = Credential('Elkwal', 'Instagram', 'Elkwal_Simple', 'Elukwal3')
        Instagram.save_credentials()
        credential_exists = Credential.find_by_site_name('Instagram')
        self.assertEqual(credential_exists, Instagram)
    def test_copy_credential(self):
        """
		Test to check if the copy a credential method copies the correct credential
		"""
        self.new_credential.save_credentials()
        Instagram = Credential('Sylvia', 'Elkwal', 'sylviaelkwal', 'Elukwal3')
        Instagram.save_credentials()
        find_credential = None
        for credential in Credential.credentials_list:
            find_credential = Credential.find_by_site_name(credential.site_name)
            pyperclip.copy(find_credential.password)
            Credential.copy_credential(self.new_credential.site_name)
            self.assertEqual('Elukwal3', pyperclip.paste())
            print(pyperclip.paste())


if __name__ == '__main__':
    unittest.main()
