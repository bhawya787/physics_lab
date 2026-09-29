import math
import unittest
from experiments import projectile, pendulum, decay, lcr, lens


class ProjectileTests(unittest.TestCase):
    def test_45_degrees(self):
        r = projectile.calculate(20, 45)
        self.assertAlmostEqual(r["vx"], r["vy"], places=6)
        self.assertAlmostEqual(r["range"], 400 / 9.8, places=4)

    def test_straight_up(self):
        r = projectile.calculate(19.6, 90)
        self.assertAlmostEqual(r["height"], 19.6, places=4)
        self.assertAlmostEqual(r["time"], 4.0, places=4)

    def test_bad_values(self):
        with self.assertRaises(ValueError):
            projectile.calculate(-5, 30)
        with self.assertRaises(ValueError):
            projectile.calculate(10, 120)


class PendulumTests(unittest.TestCase):
    def test_period(self):
        r = pendulum.calculate(1)
        self.assertAlmostEqual(r["period"], 2.0071, places=3)

    def test_frequency_is_inverse(self):
        r = pendulum.calculate(2.5)
        self.assertAlmostEqual(r["period"] * r["frequency"], 1.0, places=6)

    def test_bad_length(self):
        with self.assertRaises(ValueError):
            pendulum.calculate(0)


class DecayTests(unittest.TestCase):
    def test_one_half_life(self):
        r = decay.calculate(1000, 5, 5)
        self.assertAlmostEqual(r["remaining"], 500, places=4)

    def test_tau(self):
        r = decay.calculate(100, 10, 0)
        self.assertAlmostEqual(r["tau"], 10 / math.log(2), places=6)
        self.assertAlmostEqual(r["remaining"], 100, places=6)

    def test_bad_values(self):
        with self.assertRaises(ValueError):
            decay.calculate(100, 0, 1)
        with self.assertRaises(ValueError):
            decay.calculate(100, 5, -1)


class LcrTests(unittest.TestCase):
    def test_resonance(self):
        f0 = 1 / (2 * math.pi * math.sqrt(0.1 * 1e-5))
        r = lcr.calculate(0.1, 1e-5, 50, 10, f0)
        self.assertAlmostEqual(r["impedance"], 50, places=4)
        self.assertAlmostEqual(r["phase"], 0, places=4)
        self.assertAlmostEqual(r["current"], 0.2, places=4)

    def test_q_factor(self):
        r = lcr.calculate(0.1, 1e-5, 10, 5, 50)
        self.assertAlmostEqual(r["q"], 10, places=4)

    def test_bad_values(self):
        with self.assertRaises(ValueError):
            lcr.calculate(0.1, 1e-5, 0, 10, 50)


class LensTests(unittest.TestCase):
    def test_image_distance(self):
        r = lens.calculate(20, 30, 4)
        self.assertAlmostEqual(r["v"], -12.0, places=4)
        self.assertAlmostEqual(r["m"], 0.4, places=4)
        self.assertAlmostEqual(r["image_height"], 1.6, places=4)

    def test_image_is_smaller(self):
        r = lens.calculate(15, 5, 2)
        self.assertTrue(0 < r["m"] < 1)

    def test_bad_values(self):
        with self.assertRaises(ValueError):
            lens.calculate(-10, 20, 3)


if __name__ == "__main__":
    unittest.main()
