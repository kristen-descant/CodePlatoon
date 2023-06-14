from User import User

my_acount = User('k-des')
my_acount.add_email_address('testEmail@test.com')
my_acount.add_full_name('Kristen Descant')
my_acount.add_home_address('55 test ave', 'palm coast', 'FL', '32137')



print(my_acount)
print(my_acount.email_address)
print(my_acount.full_name)
print(my_acount.home_adress)