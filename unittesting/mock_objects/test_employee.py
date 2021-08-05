import unittest
from unittest.mock import patch

from employee import Employee


class EmployeeTest(unittest.TestCase):
    # Before running every test case, the setUp method will be get called.
    # The setUp method is used to run a code that repeats in every test cases for doing the initial setup.
    def setUp(self):
        self.employee1 = Employee("Robert", 50000)
        self.employee2 = Employee("Andrew", 60000)

    # After every test case is finished, then the tearDown method will be called and then next test case will be executed.
    # The tearDown method is used for removing the resources that we have created for a test like database for testing, etc.
    def tearDown(self):
        pass

    def test_monthly_schedule(self):
        with patch("employee.requests.get") as mocked_get:
            # For response code 200
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = "Success"

            schedule = self.employee1.monthly_schedule("July")
            mocked_get.assert_called_with("https://company.com/Robert/July")
            self.assertEqual(schedule, "Success")

            # For error code
            mocked_get.return_value.ok = False

            schedule = self.employee2.monthly_schedule("May")
            mocked_get.assert_called_with("https://company.com/Andrew/May")
            self.assertEqual(schedule, "Bad Response!")


if __name__ == '__main__':
    unittest.main()
