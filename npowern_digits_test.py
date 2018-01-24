import npowern_digits as nd
import unittest

class npowern_tester(unittest.TestCase):
    def test_adjust_digits(self):
        self.assertEqual(nd.adjust_digits(0,2),'00')
        self.assertEqual(nd.adjust_digits(1,2),'01')
        self.assertEqual(nd.adjust_digits(10,2),'10')
    def test_get_npowern_digits(self):
        self.assertEqual(nd.get_npowern_digits(1,2),'01')
        self.assertEqual(nd.get_npowern_digits(2,2),'04')
        self.assertEqual(nd.get_npowern_digits(3,2),'27')
        self.assertEqual(nd.get_npowern_digits(10,2),'00')
        self.assertEqual(nd.get_npowern_digits(126,2),'76')
        self.assertEqual(nd.get_npowern_digits(50,2),'00')
        self.assertEqual(nd.get_npowern_digits(9,2),'89')
        self.assertEqual(nd.get_npowern_digits(61,2),'61')
        self.assertEqual(nd.get_npowern_digits(31,2),nd.adjust_digits(int(31**31%100),2))
        self.assertEqual(nd.get_npowern_digits(235,2),nd.adjust_digits(int((235**235)%100),2))
        self.assertEqual(nd.get_npowern_digits(531,2),nd.adjust_digits(int((531**531)%100),2))
        self.assertEqual(nd.get_npowern_digits(2362,2),nd.adjust_digits(int((2362**2362)%100),2))
        self.assertEqual(nd.get_npowern_digits(2362,3),nd.adjust_digits(int((2362**2362)%1000),3))
        self.assertEqual(nd.get_npowern_digits(1254,3),nd.adjust_digits(int((1254**1254)%1000),3))
        self.assertEqual(nd.get_npowern_digits(4587,5),nd.adjust_digits(int((4587**4587)%100000),5))

            

unittest.main()
