class User:
    def __init__(self, user_name):
        self.user_name = user_name
        self.full_name = ''
        self.phone_number = ''
        self.email_address = ''
        self.home_adress = {
            'street_address': '',
            'city': '',
            'state': '',
            'zip_code': ''
        }
    
    def __str__(self):
        return f"{self.user_name}'s account"
              
    def add_full_name(self, full_name):
        self.full_name = full_name
    
    def add_phone_number(self, phone_number):
        self.phone_number = str(phone_number)

    def add_email_address(self, email_address):
        self.email_address = email_address

    def add_home_address(self, street_address, city, state, zip_code):
        self.home_adress['street_address'] = street_address
        self.home_adress['city'] = city
        self.home_adress['state'] = state
        self.home_adress['zip_code'] = zip_code