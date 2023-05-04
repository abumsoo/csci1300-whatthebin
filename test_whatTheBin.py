import unittest

from whatTheBin import decToBin

class TestDecToBin(unittest.TestCase):
    def test_decToBin(self):
        """

        """
        data = [1, 1, 1]
        result = decToBin(data)
        self.assertEqual(result, "00000001 00000001 00000001")

if __name__ == '__main__':
    unittest.main()