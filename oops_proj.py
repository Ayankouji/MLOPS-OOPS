class chatbook:


    __user_id = 0



    def __init__(self):
        self.__name = "Default user"
        self.id = chatbook.__user_id
        chatbook.__user_id += 1
        self.username = ""
        self.password = ""
        self.loggedin = False
        # self.menu()

    @staticmethod
    def get_id():
        return chatbook.__user_id
    
    @staticmethod
    def set_id(val):
        chatbook.__user_id = val

    def get_name(self):
        return self.__name
    
    def set_name(self,value):
        self.__name = value

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
            self.my_post()
        elif user_input == "4":
            self.sendmsg()
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

    def my_post(self):
        if self.loggedin == True:
            txt = input("What do you want to post? ")
            print(f"Following content has been posted {txt}")
        else:
            print("You need to do Signin first to post something ")
        print("\n")
        self.menu()

    def sendmsg(self):
        if self.loggedin == True:
            txt = input("Enter your message here ")
            frd = input("Whom to send the message to? ")
            print(f"Your message {txt} has been sent to {frd} ")
        else:
            print("You need to do Signin first to send message ")
            print("\n")
            self.menu()
            


# sam = chatbook()
