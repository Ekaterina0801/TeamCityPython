import unittest
import simpleNumbers
class TestPrime(unittest.TestCase):

    def test_1(self):
        self.assertEqual(simpleNumbers.is_prime(13,10), True, "Should be True")

    def test_2(self):
        self.assertEqual(simpleNumbers.is_prime(12,10), False, "Should be False")

    def test_fail(self):
        self.assertNotEqual(simpleNumbers.is_prime(14,10),True, "Should be not True")
        
if __name__=='__main__':
    unittest.main()
