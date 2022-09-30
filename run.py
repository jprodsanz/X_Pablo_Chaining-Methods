# re mem = rewards member
# gcp = gold card points 

class User: 
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_re_mem = False
        self.gcp = 0


    def display_info(self):
        print(f"=============================")
        print(f"First name: {self.first_name}")
        print(f"Last name: {self.last_name}")
        print(f"Email: {self.email}")
        print(f"Age: {self.age}")
        print(f"Member: {self.is_re_mem}")
        print(f"Current Points: {self.gcp}")
        print(f"=============================")
        return self

    def enroll(self):
        self.is_re_mem = True
        self.gcp = 200
    
    def spend_points(self, amount):
        self.gcp -= amount 

my_user = User("Pablo", "Diez", "jprodsanz@gmail.com", 31)
my_user.display_info().enroll().spend_points(84)

