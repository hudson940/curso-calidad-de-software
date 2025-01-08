import unittest
from ejercicio1 import mult, divide, length, reverse, remove_letter, even_numbers, odd_numbers, is_even

class TestEjercicio1(unittest.TestCase):

    def test_mult(self):
        self.assertEqual(mult(3), 24)
        self.assertEqual(mult(0), 0)
        self.assertEqual(mult(-1), -6)

    def test_divide(self):
        self.assertEqual(divide(8, 2), 4)
        self.assertEqual(divide(9, 3), 3)
        with self.assertRaises(ZeroDivisionError):
            divide(1, 0)

    def test_length(self):
        self.assertEqual(length([2, 3, 5, 2]), "Less than 5")
        self.assertEqual(length("Prueba"), "Longer than 5")
        self.assertEqual(length(""), "Less than 5")

    def test_reverse(self):
        self.assertEqual(reverse("casa"), "asac")
        self.assertEqual(reverse(""), "")
        self.assertEqual(reverse("a"), "a")

    def test_remove_letter(self):
        self.assertEqual(remove_letter('a', 'casa'), 'cs')
        self.assertEqual(remove_letter('b', 'casa'), 'casa')
        self.assertEqual(remove_letter('a', ''), '')

    def test_even_numbers(self):
        self.assertEqual(even_numbers([1, 8, 3, 6, 12, 5]), [8, 6, 12])
        self.assertEqual(even_numbers([1, 3, 5]), [])
        self.assertEqual(even_numbers([2, 4, 6]), [2, 4, 6])

    def test_odd_numbers(self):
        self.assertEqual(odd_numbers([1, 8, 3, 6, 12, 5]), [1, 3, 5])
        self.assertEqual(odd_numbers([2, 4, 6]), [])
        self.assertEqual(odd_numbers([1, 3, 5]), [1, 3, 5])

    def test_is_even(self):
        self.assertTrue(is_even(2))
        self.assertFalse(is_even(3))
        self.assertTrue(is_even(0))

if __name__ == '__main__':
    unittest.main()