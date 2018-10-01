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


    def copy_credential(account_name):
        """
    	Function to copy a credentials details to the clipboard
    	"""
        return Credential.copy_credential(account_name)


    def main():
        print(' ')
        print('Hey! Welcome to Password Manager.')
        while True:
            print(' ')

            print('Use these codes to navigate: \n ca-Create an Account \n li-Log In \n ex-Exit')
            short_code = input('Enter a choice: ').lower().strip()
            if short_code == 'ex':
                break
            elif short_code == 'ca':
                print("-" * 10)
                print(' ')
                print('To create a new account:')
                first_name = input('Enter your first name - ').strip()
                last_name = input('Enter your last name - ').strip()
                password = input('Enter your password - ').strip()
                save_user(create_user(first_name, last_name, password))
                print(" ")
                print(f'New Account Created for: {first_name} {last_name} using password: {password}')
            elif short_code == 'li':
                print("-" * 10)
                print(' ')
                print('To login, enter your account details:')
                user_name = input('Enter your first name - ').strip()
                password = str(input('Enter your password - '))
                user_exists = verify_user(user_name, password)
                if user_exists == user_name:
                    print(" ")
                    print(f'Hello {user_name}. Please enter an option.')
                    print(' ')
                    while True:
                        print("-" * 10)
                        print(
                            'Navigation codes: \n cc-Create a Credential \n dc-Display Credentials \n copy-Copy Password \n ex-Exit')
                        short_code = input('Enter a choice: ').lower().strip()
                        print("-" * 10)
                        if short_code == 'ex':
                            print(" ")
                            print(f'bye {user_name}')
                            break
                        elif short_code == 'cc':
                            print(' ')
                            print('Enter credential details:')
                            account_name = input('Enter the account\'s name- ').strip()
                            account_name = input('Enter your account\'s name - ').strip()
                            while True:
                                print(' ')
                                print("-" * 10)
                                print(
                                    'Please choose an option for entering a password: \n ep-enter existing password \n gp-generate a password \n ex-exit')
                                psw_choice = input('Enter an option: ').lower().strip()
                                print("-" * 10)
                                if psw_choice == 'ep':
                                    print(" ")
                                    password = input('Enter your password: ').strip()
                                    break
                                elif psw_choice == 'gp':
                                    password = create_password()
                                    break
                                elif psw_choice == 'ex':
                                    break
                                else:
                                    print('Wrong option entered. Try again.')
                            save_credential(create_credential(user_name, account_name, account_name, password))
                            print(' ')
                            print(
                                f'Credential Created: Site Name: {account_name} - Account Name: {account_name} - Password: {password}')
                            print(' ')
                        elif short_code == 'dc':
                            print(' ')
                            if display_credentials(user_name):
                                print('Here is a list of all your credentials')
                                print(' ')
                                for credential in display_credentials(user_name):
                                    print(
                                        f'Site Name: {credential.account_name} - Account Name: {credential.account_name} - Password: {credential.password}')
                                print(' ')
                            else:
                                print(' ')
                                print(" no credentials saved yet")
                                print(' ')
                        elif short_code == 'copy':
                            print(' ')
                            chosen_account = input('Enter the account name for the credential password to copy: ')
                            copy_credential(chosen_account)
                            print('')
                        else:
                            print('Wrong option entered.')

                else:
                    print(' ')
                    print(' Try again or Create an Account.')

            else:
                print("-" * 10)
                print(' ')
                print(' Try again.')


    if __name__ == '__main__':
        main()
