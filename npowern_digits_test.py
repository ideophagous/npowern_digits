import npowern_digits as nd
import unittest

class npowern_tester(unittest.TestCase):
    def test_adjust_digits(self):
        self.assertEqual(nd.adjust_digits(0),'00')
        self.assertEqual(nd.adjust_digits(1),'01')
        self.assertEqual(nd.adjust_digits(10),'10')
    def test_get_npowern_digits(self):
        self.assertEqual(nd.get_npowern_digits(1),'01')
        self.assertEqual(nd.get_npowern_digits(2),'04')
        self.assertEqual(nd.get_npowern_digits(3),'27')
        self.assertEqual(nd.get_npowern_digits(10),'00')
        self.assertEqual(nd.get_npowern_digits(126),'76')
        self.assertEqual(nd.get_npowern_digits(50),'00')
        self.assertEqual(nd.get_npowern_digits(9),'89')
        self.assertEqual(nd.get_npowern_digits(61),'61')
        self.assertEqual(nd.get_npowern_digits(31),nd.adjust_digits(int(31**31%100)))
        self.assertEqual(nd.get_npowern_digits(235),nd.adjust_digits(int((235**235)%100)))
        self.assertEqual(nd.get_npowern_digits(531),nd.adjust_digits(int((531**531)%100)))
        self.assertEqual(nd.get_npowern_digits(2362),nd.adjust_digits(int((2362**2362)%100)))

            

unittest.main()
