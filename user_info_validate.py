"""
    @File :   user_info_validate.py
    @Author : mukul
    @Date :   21-12-2021
    desc: In this user registration, we have applied regular expression
        to check the input is correct or not, if user input is Input is Invalid,
        then we are raising an exception.
"""
import re
from user_custom_exception import UserCustomException


class UserDetail:
    """
        desc: In this user registration, we have applied regular expression
        to check the input is correct or not, if user input is Empty or Invalid,
        then we are raising an exception.
    """
    @property
    def first_name(self):
        """
            return: first name
        """
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        """
            desc: assign parameter to first name
            param: value
        """
        if value == "":
            raise UserCustomException("Input is Empty")
        if re.match("^[A-Z]{1}[a-z]{2,}$", value):
            self._first_name = value
            print("Valid")
        else:
            raise UserCustomException("First Name is Invalid")

    @property
    def last_name(self):
        """
            return: last name
        """
        return self._last_name

    @last_name.setter
    def last_name(self, value):
        """
            desc: assign parameter to last name
            param: value
        """
        if value == "":
            raise UserCustomException("Input is Empty")
        if re.match("^[A-Z]{1}[a-z]{2,}$", value):
            self._last_name = value
            print("Valid")
        else:
            raise UserCustomException("Last Name is Invalid")

    @property
    def email_id(self):
        """
            return: email id
        """
        return self._email_id

    @email_id.setter
    def email_id(self, value):
        """
            desc: assign parameter to email id
            param: value
        """
        if value == "":
            raise UserCustomException("Input is Empty")
        elif re.match("^[a-zA-z0-9]+([.][0-9a-zA-z]+)*@[a-zA-z]+.[a-z]{2,3}([.][a-z]{2,3})*$", value):
            self._email_id = value
            print("Valid")
        else:
            raise UserCustomException("Email Id is Invalid")

    @property
    def mobile_num(self):
        """
            return: mobile number
        """
        return self._mobile_num

    @mobile_num.setter
    def mobile_num(self, value):
        """
            desc: assign parameter to mobile number
            param: value
        """
        if value == "":
            raise UserCustomException("Input is Empty")
        elif re.match("^[0-9]{1,3}[ : ][0-9]{10}$", value):
            self._mobile_num = value
            print("Valid")
        else:
            raise UserCustomException("Mobile Number is Invalid")

    @property
    def password(self):
        """
            return: password
        """
        return self._password

    @password.setter
    def password(self, value):
        """
            desc: assign parameter to password
            param: value
        """
        if value == "":
            raise UserCustomException("Input is Empty")
        elif re.match("^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[@#$%^&+=]).{8,}$", value):
            self._password = value
            print("Valid")
        else:
            raise UserCustomException("Password is Invalid")


user = UserDetail()

try:
    user.first_name = input("Enter First Name: ")
except UserCustomException as exc:
    print(exc.__str__())

try:
    user.last_name = input("Enter Last Name: ")
except UserCustomException as exc:
    print(exc.__str__())

try:
    user.email_id = input("Enter Email: ")
except UserCustomException as exc:
    print(exc.__str__())

try:
    user.mobile_num = input("Enter Mobile Number: ")
except UserCustomException as exc:
    print(exc.__str__())

try:
    user.password = input("Enter Password: ")
except UserCustomException as exc:
    print(exc.__str__())
