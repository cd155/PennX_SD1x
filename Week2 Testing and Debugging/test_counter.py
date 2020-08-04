import unittest
from counter import Counter

class TestCounterCase(unittest.TestCase):
    def setUp(self):
        self.counter = Counter()

    def tearDown(self):
        self.counter = None

    def test_increment(self):
        self.assertEqual(self.counter.increment(), 1)
        self.assertEqual(self.counter.increment(), 2)

    def test_decrement(self):
        self.assertEqual(self.counter.decrement(), -2)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestCounterCase)
    unittest.TextTestRunner(verbosity=2).run(suite)