class chatbot:
    def __init__(self):
        self.username = ""
        self.password = ""
        self.loggedin = False
        self.menu()

    def menu(self):
        user_input = input("""welcome to chatbot?
                        1. Press 1 to signup
                        2. Press 2 to signin
                        3. Press 3 to write a post
                        4. Press 4 to message a friends
                        5. Press any key to exit""")
        
        if user_input == '1':
            self.signup()
        elif user_input == '2':
            self.signin()
        elif user_input == '3':
            self.my_post()
        elif user_input == '4':
            self.sendmsg()
        else:
            exit()

    def signup(self):
        email = input("enter your email here")
        pwd = input("enter your password")
        self.username = email
        self.password = pwd
        print("You have signup successfully !! ")
        print("\n")
        self.menu()
    
    def signin(self):
        if self.username=="" and self.password=="":
            print("please signup firts by pressing 1 in main menu!")
        else:
            uname = input("enter your email/username:")
            pwd = input("enter your password")
            if self.username==uname and self.password==pwd:
                print("you have logged in successfully !! ")
                self.loggedin = True
            else:
                print("incorrect username...")
        print("\n")
        self.menu()

    def my_post(self):
        if self.loggedin == True:
            txt = input("enter your message here:")
            print(f"following content has been posted -> {txt}")
        else:
            print("you need to sign in first")
            self.menu()

    def sendmsg(self):
        if self.loggedin == True:
            txt = input("enter your messgae")
            frnd = input("who to send the messgae")
            print(f"your message has been send to {frnd }")
        else:
            print("you need to sign in first")
            self.menu()
        
user1 = chatbot()
