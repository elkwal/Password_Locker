# Password Locker
#### This is a python application that allows a user to generate and store passwords for various accounts.
## Author [Syvia Elukwal](https:)
## Description
Password Locker is a terminal run app that allows users to store details i.e. usernames and passwords of their various accounts.
Password Locker is a terminal run python application that allows users to store details i.e. usernames and passwords of their various accounts.
## User Stories
These are the behaviours/features that the application implements for use by a user.
As a user I would like:
* To create an account with my details - log in and password
* Store my existing login credentials
@@ -17,14 +17,14 @@ As a user I would like:
## Specifications
| Behaviour | Input | Output |
| :---------------- | :---------------: | ------------------: |
| Display codes for navigation | **in terminal $./password_locker.py** | Welcome choose an option: ca - Create Account, li - Log In, ex - Exit |
| Display prompt for creating an account | **ca** | Enter your first name, last name and password |
| Display prompt for login in | **li** | Enter your account name and password |
| Display codes for navigation | **successful login** | Choose an option: cc - Create Credential, dc - Display Credentials, copy - Copy Credential, ex - exit |
| Display prompt for creating a credential | **cc** | Enter the site name, your username and password |
| Display a list of credentials | **dc** | list of saved credentials |
| Display prompt for which credential to copy | **copy** | details of the copied credential saved to clipboard |
| Exit application | **ex** | Exit the current navigation stage |
| Display codes for navigation | **In terminal: $./main.py** | Welcome, choose an option: ca-Create Account, li-Log In, ex-Exit |
| Display prompt for creating an account | **Enter: ca** | Enter your first name, last name and password |
| Display prompt for login in | **Enter: li** | Enter your account name and password |
| Display codes for navigation | **Successful login** | Choose an option: cc - Create Credential, dc - Display Credentials, copy - Copy Credential, ex - exit |
| Display prompt for creating a credential | **Enter: cc** | Enter the site name, your username and password |
| Display a list of credentials | **Enter: dc** | Prints a list of saved credentials |
| Display prompt for which credential to copy | **Enter: copy** | Enter the site name of the credential you wish to copy. |
| Exit application | **Enter: ex** | Exit the current navigation stage |
## SetUp / Installation Requirements
