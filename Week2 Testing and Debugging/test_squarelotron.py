import unittest
from squarelotron import Squarelotron

class TestSquarelotron(unittest.TestCase):
    def setUp(self):
        self.sample = Squarelotron(5)

    def tearDown(self):
        self.sample = None

    def test_upside_down_flip(self):
        self.assertEqual(self.sample.squarelotron, [])

    def test_main_diagonal_flip(self):
        self.assertEqual(self.sample.squarelotron, [])
    
    def test_rotate_right(self):
        for number_of_turns in [-1, 0, 1]:
            self.sample.rotate_right(number_of_turns)
            self.assertEqual(self.sample.squarelotron, [])

if __name__ == '__main__':
    unittest.main()