import unittest
from employee import Employee


class EmployeeTest(unittest.TestCase):
    # The setUpClass method runs once before (at very beginning) execution of any test cases.
    @classmethod
    def setUpClass(cls):
        print("Setup class method")

    # After all of the tests are executed, then the tearDownClass method will run once.
    @classmethod
    def tearDownClass(cls):
        print("Teardown class method")

    # Before running every test case, the setUp method will be get called.
    # The setUp method is used to run a code that repeats in every test cases for doing the initial setup.
    def setUp(self):
        self.employee1 = Employee("Robert", 50000)
        self.employee2 = Employee("Andrew", 60000)

    # After every test case is finished, then the tearDown method will be called and then next test case will be executed.
    # The tearDown method is used for removing the resources that we have created for a test like database for testing, etc.
    def tearDown(self):
        pass

    def test_employee_name(self):
        self.assertEqual(self.employee1.get_name, "Robert")
        self.assertEqual(self.employee2.get_name, "Andrew")

        self.employee1.name = "Rob"
        self.employee2.name = "P"

        self.assertEqual(self.employee1.get_name, "Rob")
        self.assertEqual(self.employee2.get_name, "P")

    def test_employee_email(self):
        self.assertEqual(self.employee1.get_email, "Robert@email.com")
        self.assertEqual(self.employee2.get_email, "Andrew@email.com")

        self.employee1.name = "Rob"
        self.employee2.name = "P"

        self.assertEqual(self.employee1.get_email, "Rob@email.com")
        self.assertEqual(self.employee2.get_email, "P@email.com")

    def test_employee_salary(self):
        self.assertEqual(self.employee1.get_salary, 50000)
        self.assertEqual(self.employee2.get_salary, 60000)

        self.employee1.salary = 80000
        self.employee2.salary = 100000

        self.assertEqual(self.employee1.salary_hike(), 84000)
        self.assertEqual(self.employee2.salary_hike(), 105000)


if __name__ == '__main__':
    unittest.main()
