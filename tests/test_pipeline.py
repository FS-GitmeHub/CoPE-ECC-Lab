"""No network, SDK, secrets, or user-project dependencies."""

import unittest

from lab_demo.pipeline import plan_tasks


class PlanTasksTests(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(plan_tasks({}), [])

    def test_deterministic(self):
        graph = {"verify": ["build", "review"], "review": ["build"], "build": []}
        self.assertEqual(plan_tasks(graph), ["build", "review", "verify"])
        self.assertEqual(plan_tasks(graph), ["build", "review", "verify"])

    def test_independent_tasks_sorted(self):
        self.assertEqual(plan_tasks({"z": [], "a": [], "m": []}), ["a", "m", "z"])

    def test_unknown_dependency(self):
        with self.assertRaisesRegex(ValueError, "unknown dependency"):
            plan_tasks({"build": ["missing"]})

    def test_duplicate_dependency(self):
        with self.assertRaisesRegex(ValueError, "duplicate dependency"):
            plan_tasks({"build": [], "verify": ["build", "build"]})

    def test_cycle(self):
        with self.assertRaisesRegex(ValueError, "cycle"):
            plan_tasks({"a": ["b"], "b": ["a"]})

    def test_self_cycle(self):
        with self.assertRaisesRegex(ValueError, "cycle"):
            plan_tasks({"a": ["a"]})

    def test_string_dependencies_forbidden(self):
        with self.assertRaises(TypeError):
            plan_tasks({"a": "test"})


if __name__ == "__main__":
    unittest.main()
