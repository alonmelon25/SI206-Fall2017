#From: https://code.tutsplus.com/tutorials/write-professional-unit-tests-in-python--cms-25835
from Car import SelfDrivingCar
import unittest
from unittest import TestCase
 
class SelfDrivingCarTest(TestCase):
    def setUp(self):
        self.car = SelfDrivingCar()

    def test_stop(self):
        self.car.speed = 5
        self.car.stop()
        # Verify the speed is 0 after stopping
        self.assertEqual(0, self.car.speed)
 
        # Verify it is Ok to stop again if the car is already stopped
        self.car.stop() 
        self.assertEqual(0, self.car.speed)


unittest.main()