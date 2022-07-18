import unittest


class TestMethods(unittest.TestCase):
    def test_string(self):
        self.assertEqual("abc","abc")


if __name__ == '__main__':
    unittest.main()
