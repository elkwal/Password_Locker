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


    
