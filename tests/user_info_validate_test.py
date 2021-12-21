import unittest
from user_info_validate import UserDetail
from user_custom_exception import UserCustomException


class MyTestCase(unittest.TestCase):
    """
     desc: Test cases for all the input values
    """
    def test_first_name_invalid_input(self):
        """
            desc: test case for invalid input for first name
        """
        try:
            param = "mukul"
            user = UserDetail()
            user.first_name = param
        except UserCustomException as exc:
            self.assertEqual("First Name is Invalid", exc.__str__())  # add assertion here

    def test_first_name_empty_value(self):
        """
            desc: test case for empty input for first name
        """
        try:
            param = ""
            user = UserDetail()
            user.first_name = param
        except UserCustomException as exc:
            self.assertEqual("Input is Empty", exc.__str__())  # add assertion here

    def test_first_name_valid_input(self):
        """
            desc: test case for valid input for first name
        """
        param = "Mukul"
        user = UserDetail()
        user.first_name = param
        self.assertEqual(param, user.first_name)  # add assertion here

    def test_last_name_invalid_input(self):
        """
            desc: test case for invalid input for last name
        """
        try:
            param = "jain"
            user = UserDetail()
            user.last_name = param
        except UserCustomException as exc:
            self.assertEqual("Last Name is Invalid", exc.__str__())  # add assertion here

    def test_last_name_empty_value(self):
        """
            desc: test case for empty input for last name
        """
        try:
            param = ""
            user = UserDetail()
            user.last_name = param
        except UserCustomException as exc:
            self.assertEqual("Input is Empty", exc.__str__())  # add assertion here

    def test_last_name_valid_input(self):
        """
            desc: test case for valid input for last name
        """
        param = "Jain"
        user = UserDetail()
        user.last_name = param
        self.assertEqual("Jain", user.last_name)  # add assertion here

    def test_email_id_invalid_input(self):
        """
            desc: test case for invalid input for email id
        """
        try:
            param = "mukuljain@102gmail.co"
            user = UserDetail()
            user.email_id = param
        except UserCustomException as exc:
            self.assertEqual("Email Id is Invalid", exc.__str__())  # add assertion here

    def test_email_id_empty_value(self):
        """
            desc: test case for empty input for email id
        """
        try:
            param = ""
            user = UserDetail()
            user.email_id = param
        except UserCustomException as exc:
            self.assertEqual("Input is Empty", exc.__str__())  # add assertion here

    def test_email_id_valid_input(self):
        """
            desc: test case for valid input for email id
        """
        param = "mukuljain102@gmail.com"
        user = UserDetail()
        user.email_id = param
        self.assertEqual(param, user.email_id)  # add assertion here

    def test_mobile_num_invalid_input(self):
        """
            desc: test case for invalid input for mobile number
        """
        try:
            param = "2154876587"
            user = UserDetail()
            user.mobile_num = param
        except UserCustomException as exc:
            self.assertEqual("Mobile Number is Invalid", exc.__str__())  # add assertion here

    def test_mobile_num_empty_value(self):
        """
            desc: test case for empty input for mobile number
        """
        try:
            param = ""
            user = UserDetail()
            user.mobile_num = param
        except UserCustomException as exc:
            self.assertEqual("Input is Empty", exc.__str__())  # add assertion here

    def test_mobile_num_valid_input(self):
        """
            desc: test case for valid input for mobile number
        """
        param = "21 1548878875"
        user = UserDetail()
        user.mobile_num = param
        self.assertEqual(param, user.mobile_num)  # add assertion here

    def test_password_invalid_input(self):
        """
            desc: test case for invalid input for password
        """
        try:
            param = "mukul123"
            user = UserDetail()
            user.password = param
        except UserCustomException as exc:
            self.assertEqual("Password is Invalid", exc.__str__())  # add assertion here

    def test_password_empty_value(self):
        """
            desc: test case for empty input for password
        """
        try:
            param = ""
            user = UserDetail()
            user.password = param
        except UserCustomException as exc:
            self.assertEqual("Input is Empty", exc.__str__())  # add assertion here

    def test_password_valid_input(self):
        """
            desc: test case for valid input for password
        """
        param = "Mmukul@12W"
        user = UserDetail()
        user.password = param
        self.assertEqual(param, user.password)  # add assertion here


if __name__ == '__main__':
    unittest.main()
