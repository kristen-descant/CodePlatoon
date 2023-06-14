class ContactList:
    def __init__(self, name_of_list, existing_contact_list):
        self._name = name_of_list
        self.contacts = existing_contact_list

    def add_contacts(self, contact_name, contact_number):
        self.contacts.append({'name': contact_name, 'number': contact_number})

    def remove_contact(self, contact_name):
        for contact in self.contacts:
            if contact['name'] == contact_name:
                self.contacts.remove(contact)

    def find_shared_contacts(self, contact_list):
        shared_contacts = []
        for contact in self.contacts:
            if contact in contact_list.contacts:
                shared_contacts.append(contact)
        return shared_contacts
    



#Tests:
# friends = [{'name':'Alice','number':'867-5309'},{'name':'Bob', 'number':'555-5555'}]
# work_buddies = [{'name':'Alice','number':'867-5309'},{'name':'Carlos', 'number':'555-5555'}]

# my_friends_list = ContactList('My Friends', friends)
# my_work_buddies = ContactList('Work Buddies', work_buddies)

# # print(my_friends_list.contacts)

# # my_friends_list.remove_contact('Bob')

# # print(my_friends_list.contacts)

# friends_i_work_with = my_friends_list.find_shared_contacts(my_work_buddies)

# print(friends_i_work_with)