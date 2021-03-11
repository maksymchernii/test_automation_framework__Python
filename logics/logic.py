import random


class RandomText():

    def get_message(self, string_length):

        chars = "abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
        message = ''

        for symb in range(string_length + 1):
            message += random.choice(chars)

        return message

