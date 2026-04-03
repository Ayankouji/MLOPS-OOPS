class chatbook:
    def __init__(self):
        self.username = ""
        self.password = ""
        self.loggedin = False
        self.menu()

    def menu(self):
        user_input = input("""Welcome to Chatbook How would you like to proceed?
                           1. Press 1 to singnup
                           2. Press 2 to signin
                           3. Press 3 to write a post
                           4.Press 4 to message friend
                           5.Press any other key to exit """)
        
        if user_input == "1":
            self.signup()
        elif user_input == "2":
            self.sigin()
        elif user_input == "3":
            pass
        elif user_input == "4":
            pass
        else:
            exit()

    
    def signup(self):
        email = input("Enter your email here ")
        pwd = input("Enter your password here ")
        self.username = email
        self.password = pwd
        print("You have successfully signed up")
        print("\n")
        self.menu()

    def sigin(self):
        if self.username == "" and self.password == "":
            print("Please signup first by pressing 1 in the main menu")
        else:
            uname = input("Enter your email here ")
            pwd = input("Enter your password here ")
            if self.username == uname and self.password == pwd:
                print("You have successfully signed in")
                self.loggedin = True
            else:
                print("Ivalid credentials,Enter correct email and password")
        print("\n")
        self.menu()



sam = chatbook()
