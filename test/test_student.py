import unittest
from class_definitions import student as t


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.student = t.Student('Duck', 'Daisy', 'English')

    def tearDown(self):
        del self.student

    def test_initial_value_required_attributes(self):
        self.assertEqual(self.student.last_name, 'Duck')
        self.assertEqual(self.student.first_name, 'Daisy')
        self.assertEqual(self.student.major, 'English')
        self.assertEqual(self.student.gpa, 0.0)

    def test_initial_all_attributes(self):
        student = t.Student('Duck', 'Daisy', 'English', 4.0)
        assert student.last_name == 'Duck'
        assert student.first_name == 'Daisy'
        assert student.major == 'English'
        assert student.gpa == 4.0

    def test_student_str(self):
        self.assertEqual(str(self.student), 'Duck, Daisy has major English with gap: 0.0')

    def test_object_not_created_error_last_name(self):
        with self.assertRaises(ValueError):
            p = t.student('123', 'Daisy')


if __name__ == '__main__':
    unittest.main()
