import unittest
import pyramid

IS_PYRAMID = "banana"
ISNT_PYRAMID = "bandana"

BAD_1 = None
BAD_2 = 3.14

class TestSimple(unittest.TestCase):

    def test_positve(self):
        self.assertTrue(pyramid.is_pyramid(IS_PYRAMID))
        self.assertFalse(pyramid.is_pyramid(ISNT_PYRAMID))

    def test_bad_input(self):
        self.assertFalse(pyramid.is_pyramid(BAD_1))
        self.assertFalse(pyramid.is_pyramid(BAD_2))


if __name__ == '__main__':
    unittest.main()
