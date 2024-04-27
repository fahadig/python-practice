# print("Fahad")
# from typing import Tuple
# data_base : list[tuple[str,str]] = [("qasim",123),
#                                      ("sirzia",456),
#                                      ("ikhlas",789)]

# for row in data_base:
#     user, password = row
#     print(user, password)


from typing import Tuple
data_base : list[tuple[str,str]] = [("qasim",123),
                                     ("sirzia",456),
                                     ("ikhlas",789)]

input_user : str  = input("Enter user name")
input_password : str  = input("Enter password")

for row in data_base:
    user, password = row
    if input_user == user and input_password == password:
        print("Valid user")
        break