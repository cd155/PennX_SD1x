import unittest
from squarelotron import Squarelotron

class TestSquarelotron(unittest.TestCase):
    def setUp(self):
        self.sample = Squarelotron(5)

    def tearDown(self):
        self.sample = None

    def test_matrix_generate(self):
        self.assertEqual(self.sample.squarelotron, [[1,2,3,4,5], [6,7,8,9,10], [11,12,13,14,15], [16,17,18,19,20], [21,22,23,24,25]])

    def test_upside_down_flip_ring_one(self):
        self.assertEqual(self.sample.upside_down_flip(1), [[21,22,23,24,25], [16,7,8,9,20], [11,12,13,14,15], [6,17,18,19,10], [1,2,3,4,5]])

    def test_upside_down_flip_ring_two(self):
        self.assertEqual(self.sample.upside_down_flip(2), [[1,2,3,4,5], [6,17,18,19,10], [11,12,13,14,15], [16,7,8,9,20], [21,22,23,24,25]])

    def test_upside_down_flip_ring_three(self):
        self.assertEqual(self.sample.upside_down_flip(3), [[1,2,3,4,5], [6,7,8,9,10], [11,12,13,14,15], [16,17,18,19,20], [21,22,23,24,25]])

    def test_main_diagonal_flip_ring_one(self):
        self.assertEqual(self.sample.main_diagonal_flip(1), [[1,6,11,16,21], [2,7,8,9,22], [3,12,13,14,23], [4,17,18,19,24], [5,10,15,20,25]])

    def test_main_diagonal_flip_ring_two(self):
        self.assertEqual(self.sample.main_diagonal_flip(2), [[1,2,3,4,5], [6,7,12,17,10], [11,8,13,18,15], [16,9,14,19,20], [21,22,23,24,25]])

    def test_main_diagonal_flip_ring_three(self):
        self.assertEqual(self.sample.main_diagonal_flip(3), [[1,2,3,4,5], [6,7,8,9,10], [11,12,13,14,15], [16,17,18,19,20], [21,22,23,24,25]])
    
    def test_rotate_right_clockwise(self):
        self.sample.rotate_right(1)
        self.assertEqual(self.sample.squarelotron, [[21,16,11,6,1], [22,17,12,7,2], [23,18,13,8,3], [24,19,14,9,4], [25,20,15,10,5]])

    def test_rotate_right_zero(self):
        self.sample.rotate_right(0)
        self.assertEqual(self.sample.squarelotron, [[1,2,3,4,5], [6,7,8,9,10], [11,12,13,14,15], [16,17,18,19,20], [21,22,23,24,25]])

    def test_rotate_right_counter_clockwise(self):
        self.sample.rotate_right(-1)
        self.assertEqual(self.sample.squarelotron, [[5,10,15,20,25], [4,9,14,19,24], [3,8,13,18,23], [2,7,12,17,22], [1,6,11,16,21]])

if __name__ == '__main__':
    unittest.main()