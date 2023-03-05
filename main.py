import unittest
import test

class TestedSpeed (unittest.TestCase):
    def speed1(self):
        self.assertEqual('Invalid', test.car_speed(-1))
    def speed2(self):
        self.assertEqual('Low', test.car_speed(39))
    def speed3(self):
        self.assertEqual('Normal', test.car_speed(119))
    def speed4(self):
        self.assertEqual('High', test.car_speed(199))
    def speed5(self):
        self.assertEqual('V.High', test.car_speed(219))
    def speed6(self):
        self.assertEqual('Invalid', test.car_speed(221))

mysuitspeed = unittest.TestSuite()
mysuitspeed.addTest(TestedSpeed())


class TestedScore (unittest.TestCase):
    def score1(self):
        self.assertEqual('Invalid', test.student_score(-1))
    def score2(self):
        self.assertEqual('Failed', test.student_score(49))
    def score3(self):
        self.assertEqual('Passed', test.student_score(64))
    def score4(self):
        self.assertEqual('Good', test.student_score(74))
    def score5(self):
        self.assertEqual('V.Good', test.student_score(84))
    def score6(self):
        self.assertEqual('Excellent', test.student_score(90))
    def score7(self):
        self.assertEqual('Invalid', test.student_score(110))

mysuitscore = unittest.TestSuite()
mysuitscore.addTest(TestedScore())



if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(mysuitspeed)
    runner.run(mysuitscore)
