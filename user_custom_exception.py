"""
    @File :   user_custom_exception.py
    @Author : mukul
    @Date :   21-12-2021
"""


class UserCustomException(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message
