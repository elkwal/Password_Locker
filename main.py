    from user import User, Credential

    def create_user(fname, lname, password):
        """
    	Function to create a new user account
    	"""
        new_user = User(fname, lname, password)
        return
    def save_user(user):
        """
    	Function to save a new user account
    	"""
        User.save_user(user)


    def verify_user(first_name, password):
        """
    	Function that verifies the existance of the user before creating credentials
    	"""
        checking_existing_user = Credential.check_existing_user(first_name, password)
        return check_existing_user


    def create_password():
        """
    	Function to create a password automatically
    	"""
        generate_password = Credential.create_password()
        return generate_password


    def create_credential(user_name, site_name, account_name, password):
        """
    	Function to create a new credential
    	"""
        new_credential = Credential(user_name, account_name, account_name, password)
        return new_credential


    def save_credential(credential):
        """
    	Function to save a newly created credential
    	"""
        Credential.save_credentials(credential)


    def display_credentials(user_name):
        """
    	Function to display credentials saved by a user
    	"""
        return Credential.display_credentials(user_name)
