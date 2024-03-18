from ..notification.Notification import Notification
import unittest

class test(unittest.TestCase):

    def setUp(self):
        # Setting up different edge cases
        self.t1 = Notification(None, "magnitude:0-5.15;area:11.54,23.45,88.3;")
        self.t2 = Notification(None, "magnitude:5.565-10;")
        self.t3 = Notification(None, "magnitude:4.23-6.15;area:4.66,2.445,29.3;")
        self.t4 = Notification(None, "area:111.54,234.45,88.3;")

    # Tests the parsing and initialization
    def testInit(self):
        self.assertEqual(self.t1.minMagnitude, 0)
        self.assertEqual(self.t1.maxMagnitude, 5.15)
        self.assertEqual(self.t1.latitude, 11.54)
        self.assertEqual(self.t1.longitude, 23.45)
        self.assertEqual(self.t1.radius, 88.3)

        self.assertEqual(self.t2.minMagnitude, 5.565)
        self.assertEqual(self.t2.maxMagnitude, 10)
        self.assertEqual(self.t2.latitude, None)
        self.assertEqual(self.t2.longitude, None)
        self.assertEqual(self.t2.radius,None)

        self.assertEqual(self.t3.minMagnitude, 4.23)
        self.assertEqual(self.t3.maxMagnitude, 6.15)
        self.assertEqual(self.t3.latitude, 4.66)
        self.assertEqual(self.t3.longitude, 2.445)
        self.assertEqual(self.t3.radius, 29.3)

        self.assertEqual(self.t4.minMagnitude,None)
        self.assertEqual(self.t4.maxMagnitude, None)
        self.assertEqual(self.t4.latitude, 111.54)
        self.assertEqual(self.t4.longitude, 234.45)
        self.assertEqual(self.t4.radius, 88.3)

    def testCompareToDatabase(self):
        self.assertTrue(self.t1.compareToDatabase(4.55, None, None, None))
        self.assertFalse(self.t2.compareToDatabase(4.55, None, None, None))



unittest.main()

