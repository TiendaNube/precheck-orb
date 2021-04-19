import unittest
import naming_validation


class TestCase(unittest.TestCase):

    def test_check_upper(self):
        self.assertFalse(naming_validation.check_upper(), False)

    def test_check_str(self):
        self.assertFalse(naming_validation.check_str(), False)

    def test_check_length(self):
        self.assertFalse(naming_validation.check_length(), False)


if __name__ == '__main__':
    unittest.main()
