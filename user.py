import pyperclip
import random
import string
class User:
    """
    Class that generates the user's information
    """


    def __init__(self, first_name, last_name, password):


        self.first_name = first_name
        self.last_name = last_name
        self.password = password

    users_list = [] #Empty users list

    def save_user(self):
        """
		This function helps in saving the created property with the password
		"""
        User.users_list.append(self)

class Credential:
    """
	Class that creates  account credentials, generate passwords and save their information
	"""

    credentials_list = []

    @classmethod
    def check_existing_user(cls, first_name, password):
        """
		Method that checks if the name and password entered match entries in the users_list
		"""
        current_user = ''
        for user in User.users_list:
            if (user.first_name == first_name and user.password == password):
                current_user = user.first_name
        return current_user

    def __init__(self, user_name, site_name, account_name, password):
        '''
		Method to define the properties for each user object will hold.
		'''

        # instance variables

        self.user_name = user_name
        self.site_name = site_name
        self.account_name = account_name
        self.password = password

    def save_credentials(self):
        """
		Function to save a newly created user instance
		"""
        Credential.credentials_list.append(self)

    def create_password(size=6, char=string.ascii_uppercase + string.ascii_lowercase + string.digits):
        """
		Function to generate an 6 character password for a credential
		"""
        generate password = ''.join(random.choice(char) for _ in range(size))
        return generate password

    @classmethod
    def display_credentials(cls, user_name):
        """
		Class method to display the list of credentials saved
		"""
        user_credentials_list = []
        for credential in cls.credentials_list:
            if credential.user_name == user_name:
                user_credentials_list.append(credential)
        return user_credentials_list

    @classmethod
    def find_by_site_name(cls, site_name):
        """
		Method that takes in a site_name and returns a credential that matches that site_name.
		"""
        for credential in cls.credentials_list:
            if credential.site_name == site_name:
                return credential
