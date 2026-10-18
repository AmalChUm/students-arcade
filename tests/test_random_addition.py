"""Exercise arithmetic and launcher-visible contributor credits."""
import contextlib
import importlib
import io
from pathlib import Path
import re
import sys
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
plugin = importlib.import_module("plugins.random_addition")
launcher = importlib.import_module("main")


class RandomAdditionReviewTests(unittest.TestCase):
    def test_extreme_values_are_added_correctly_with_a_clear_result(self):
        for operands, result in [((1, 1), 2), ((100, 100), 200), ((1, 100), 101)]:
            with self.subTest(operands=operands):
                with patch.object(plugin.random, "randint", side_effect=operands):
                    self.assertEqual(plugin.run(), f"Number Addition complete: {operands[0]} + {operands[1]} = {result}")

    def test_normal_random_equations_are_correct(self):
        for _ in range(100):
            match = re.search(r"(\d+) \+ (\d+) = (\d+)$", plugin.run())
            self.assertIsNotNone(match)
            first, second, total = map(int, match.groups())
            self.assertTrue(1 <= first <= 100)
            self.assertTrue(1 <= second <= 100)
            self.assertEqual(total, first + second)

    def test_launcher_displays_both_contributors_and_runs_addition_once(self):
        stream = io.StringIO()
        with contextlib.redirect_stdout(stream):
            launcher.main()
        output = stream.getvalue()
        self.assertIn("Number Addition by Gaige Szy and Andrew Haralambous", output)
        self.assertEqual(output.count("Number Addition by "), 1)
        self.assertIn("Number Addition complete:", output)
        self.assertNotIn("[error]", output)


if __name__ == "__main__":
    unittest.main(verbosity=2)
