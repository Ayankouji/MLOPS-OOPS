from oops_proj import chatbook
#Modular coding
user1 = chatbook()
print(user1.id)


#using static method directly from class rather than obj
chatbook.set_id(10)

user2 = chatbook()
print(user2.id)

user3 = chatbook()
print(user3.id)

# print()
# user2 = chatbook()
# print(user2.id)

# user3 = chatbook()
# print(user3.id)



# print(user1._chatbook__name) -> To accesss private variable outside the class


#Getter & Setter method
# print(user1.get_name())
# user1.set_name("Agent")
# print(user1.get_name())

