import unittest
import divide


class DivideTest(unittest.TestCase):
    def test_divide(self):
        self.assertEqual(divide.divide(4, 2), 2)
        self.assertEqual(divide.divide(-2, 2), -1)
        self.assertEqual(divide.divide(-8, -2), 4)
        self.assertEqual(divide.divide(5, 2), 2.5)

        # Check the raises
        self.assertRaises(ValueError, divide.divide, 5, 0)

        # Best way to test raises is using context managers
        with self.assertRaises(ValueError):
            divide.divide(10, 0)


if __name__ == '__main__':
    unittest.main()
