class User:

    all_posts = {}

    def __init__(self, user_name):
        self.user_name = user_name
        self._full_name = ''
        self._phone_number = ''
        self._email_address = ''
        self._home_adress = {
            'street_address': '',
            'city': '',
            'state': '',
            'zip_code': ''
        }
    
    
    def __str__(self):
        return f"{self.user_name}'s account"

    @property
    def full_name(self):
        return self._full_name
    
    @full_name.setter
    def add_full_name(self, full_name):
        self._full_name = full_name
    
    @property
    def phone_number(self):
        return self._phone_number
    
    @phone_number.setter
    def add_phone_number(self, phone_number):
        self._phone_number = str(phone_number)

    @property
    def email_address(self):
        return self._email_address
    
    @email_address.setter
    def add_email_address(self, email_address):
        self._email_address = email_address

    @property
    def home_address(self):
        return self._home_adress
    
    def add_home_address(self, street_address, city, state, zip_code):
        self._home_adress['street_address'] = street_address
        self._home_adress['city'] = city
        self._home_adress['state'] = state
        self._home_adress['zip_code'] = zip_code

    def new_post(self, postStr):
        if self.user_name not in User.all_posts:
            User.all_posts[self.user_name] = [Post(postStr)]
        else:
             User.all_posts[self.user_name].append(Post(postStr))
    
    @classmethod
    def output_posts(cls):
        outputStr = ''
        for key in cls.all_posts:
            outputStr += key + ':\n'
            for post in cls.all_posts[key]:
                outputStr += '\t' + str(post.id) + ': ' + post.text + '\n'
        return outputStr

    @classmethod
    def delete_post(cls, postId):
        for key in cls.all_posts:
            for post in cls.all_posts[key]:
                if str(post.id) == postId:
                    cls.all_posts[key].remove(post)

class Post:
    counter = 0

    def __init__(self, text):
        self.text = text
        self.id = Post.counter
        Post.counter += 1



my_acount = User('k-des')
my_acount.add_email_address = 'testEmail@test.com'
my_acount.add_full_name = 'Kristen Descant'
my_acount.add_home_address('55 test ave', 'palm coast', 'FL', '32137')
my_acount.new_post('my first post')
my_acount.new_post('my second post')

new_account = User('newperson')
new_account.new_post('a new user post')

# input = input('post to remove: ')


# print(User.all_posts)
# print(User.output_posts())


# User.delete_post(input)

# print(User.output_posts())


# print(my_acount)
# print(my_acount.email_address)
# print(my_acount.full_name)
# print(my_acount.home_adress)