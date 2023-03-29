from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from hoverable import HoverBehavior
from kivy.uix.image import Image
from kivy.uix.behaviors import ButtonBehavior
import json, glob
from datetime import datetime
from pathlib import Path
import random

Builder.load_file('design.kv')    # Load the .kv file for the app's UI design

# Define the LoginScreen class, which inherits from kivy.uix.screenmanager.Screen
class LoginScreen(Screen):
    def sign_up(self):
        self.manager.current = 'sign_up_screen'    # Switch to the sign up screen
        
    def login(self, uname, pword):
        with open('users.json') as file:    # Open the users.json file
            users = json.load(file)    # Load the user data from the file
        if uname in users and users [uname]['password'] == pword:    # Check if the username and password match the data
            self.manager.current = 'login_screen_success'    # Switch to the login success screen if the login is successful
        else:
            self.ids.login_wrong.text = 'Wrong Username or Password !'    # Dsplay an error message if the login fails

# Define the RootWidget class, which inherits from kivy.uix.screenmanager.ScreenManager
class RootWidget(ScreenManager):
    pass

# Define the SignUpScreen class, which inherits from kivy.uix.screenmanager.Screen
class SignUpScreen(Screen):
    def add_user(self, uname, pword):
        with open('users.json') as file:    # Open the users.json file
            users = json.load(file)     # Load the user data from the file
            
        users[uname] = {'username' : uname, 
                        'password' : pword,
                        'created' : datetime.now().strftime('%Y-%m-%d %H-%M-%S')}    # Add the new user to the data dictionary
        
        with open('users.json', 'w') as file:    # Write the updated user data to the file
            json.dump(users, file)
        self.manager.current = 'sign_up_screen_success'   # Switch to the sign up success screen
        
# Define the SignUpScreenSuccess class, which inherits from kivy.uix.screenmanager.Screen
class SignUpScreenSuccess(Screen):
    def go_to_login(self):
        self.manager.transition.direction = 'right'   # Set the transition direction
        self.manager.current = 'login_screen'    # Switch to the login screen
            
# Define the LoginScreenSuccess class, which inherits from kivy.uix.screenmanager.Screen
class LoginScreenSuccess(Screen):
    def log_out(self):
        self.manager.transition.direction = 'right'    # Set the transition direction
        self.manager.current = 'login_screen'    # Switch to the login screen
    
    def get_quote(self, feel):
        feel = feel.lower()
        available_feelings = glob.glob('quotes/*txt')    # Get all available .txt files in the 'quotes' directory
        
        available_feelings = [Path(filename).stem for filename in 
                              available_feelings]    # Get the stem of each filename (i.e. the filename without the extension)
        
        if feel in available_feelings:
            with open(f'quotes/{feel}.txt') as file:    # Open the file containing the quotes for the given feeling
                quotes = file.readlines()    # Read all lines of the file
            self.ids.quote.text = random.choice(quotes)    # Choose a random quote from the file and display it
        else:
            self.ids.quote.text = 'Try another feeling'     # Display an error message if the given feeling does not   
        
class ImageButton(ButtonBehavior, HoverBehavior, Image):
    pass        
        
# Define the MainApp class, which inherits from kivy.app.App
class MainApp(App):
    def build(self):
        return RootWidget()    # Build and return the root widget for the app

# If the file is run directly, create an instance of the MainApp class and run the app
if __name__ == '__main__':
    MainApp().run()
    