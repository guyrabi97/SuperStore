import re

class Client:

    def __init__(self,client_id,name,email,address,phone_number,gender):
        self.client_id = client_id
        self.name = name
        self.email = email
        self.address = address
        self.phone_number = phone_number
        self.gender = gender
        correct_email = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        if (re.fullmatch(correct_email, email)):
            pass
        else:
            self.email="invalid email"
        if len(str(phone_number))!=10:
            self.phone_number="incorrect number, check if you have 10 digits"

        if gender != 'm' and gender!= "M" and gender!= 'f' and gender!= "F":
            self.gender="M"
    def print_me(self):
        print(f"----{self.client_id}----\nname:{self.name}\nemail:{self.email}\n"
              f"address:{self.address}\nphone_number:{self.phone_number}\ngender:{self.gender}")

    def __str__(self):
        return f"{self.client_id},{self.name},{self.email},{self.address},{self.phone_number},{self.gender}"

    def __repr__(self):
        return str(self)

