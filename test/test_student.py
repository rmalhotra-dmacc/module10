import unittest
from class_definitions import student as t


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.person = t.Student('Duck', 'Daisy', 'English', 4.0)

    def tearDown(self):
        del self.person

    def test_initial_value_required_attributes(self):
        self.assertEqual(self.person.last_name, 'Duck')
        self.assertEqual(self.person.first_name, 'Daisy')


if __name__ == '__main__':
    unittest.main()
