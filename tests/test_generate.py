import unittest
from number_operation import isPrime, generatePrimeNumber

class TestIsPrime(unittest.TestCase):

    def test_prime_number(self):
        self.assertEqual(isPrime(5), True)
        
    def test_other_prime_number(self):
        self.assertEqual(isPrime(769), True)
        
    def test_not_prime_number(self):
        self.assertEqual(isPrime(15), False)

    def test_other_not_prime_number(self):
        self.assertEqual(isPrime(377), False)

    def test_list_prime_number(self):
        self.assertEqual(generatePrimeNumber(15), [2,3,5,7,11,13])
    
    def test_list_not_prime(self):
        self.assertEqual(generatePrimeNumber(1), [])

    def test_empty_list(self):
        self.assertEqual(generatePrimeNumber(0), [])


if __name__ == '__main__':
    unittest.main()
