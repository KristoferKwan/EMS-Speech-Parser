access_token = '7J2X2UTJFDJ4FMPUQJ7ELNNOH5MUYHMD'

from wit import Wit

str_input = input("Enter your message: ")
print(str_input)

client = Wit(access_token)
print(client.message(str_input))


