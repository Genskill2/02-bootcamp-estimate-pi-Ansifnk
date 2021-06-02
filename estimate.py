import math
import unittest
import random


class TestWallis(unittest.TestCase):
    def test_low_iters(self):
        for i in range(0, 5):
            pi = wallis(i)
            self.assertTrue(abs(pi - math.pi) > 0.15,
                            msg=f"Estimate with just {i} iterations is {pi} which is too accurate.\n")

    def test_high_iters(self):
        for i in range(500, 600):
            pi = wallis(i)
            self.assertTrue(abs(pi - math.pi) < 0.01,
                            msg=f"Estimate with even {i} iterations is {pi} which is not accurate enough.\n")


class TestMC(unittest.TestCase):
    def test_randomness(self):
        pi0 = monte_carlo(15000)
        pi1 = monte_carlo(15000)

        self.assertNotEqual(
            pi0, pi1, "Two different estimates for PI are exactly the same. This is almost impossible.")

        self.assertFalse(abs(
            pi0 - pi1) > 0.05, "Two different estimates of PI are too different. This should not happen")

    def test_accuracy(self):
        for i in range(500, 600):
            pi = monte_carlo(i)
            self.assertTrue(abs(pi - math.pi) < 0.4,
                            msg=f"Estimate with even {i} iterations is {pi} which is not accurate enough.\n")


if __name__ == "__main__":
    unittest.main()


def wallis(n):
    j = 1
    n = int(n)

    for i in range(n):
        pi = pi*((4*(j*j))/(4*(j*j)-1))
        j += 1
    print(pi)
    return 2*pi


def monte_carlo(n):
    outside = 0
    inside = 0
    pi = 0
    n = int(n)
    for i in range(n):

        j = random.random()
        i = random.random()

        if(((i**2+j**2)**0.5) > 1):
            outside += 1

        else:
            inside += 1
    pi = (inside/(outside+inside))*4
    return pi
