import unittest

import pandas as pd

from normalizedformtables import closure, onenormal_form, powerset, superkey


class NormalizationHelperTests(unittest.TestCase):
    def test_closure_follows_transitive_dependencies(self):
        dependencies = {
            ("student_id",): ["department_id"],
            ("department_id",): ["department_name"],
        }

        result = closure({"student_id"}, dependencies)

        self.assertEqual(
            result,
            {"student_id", "department_id", "department_name"},
        )

    def test_superkey_detects_unique_and_repeated_determinants(self):
        relation = pd.DataFrame(
            {
                "student_id": [1, 2, 3],
                "department": ["CS", "CS", "EE"],
            }
        )

        self.assertTrue(superkey(relation, {"student_id"}))
        self.assertFalse(superkey(relation, {"department"}))

    def test_one_normal_form_rejects_collection_values(self):
        atomic = pd.DataFrame({"student_id": [1, 2], "course": ["DB", "AI"]})
        non_atomic = pd.DataFrame(
            {"student_id": [1, 2], "course": [["DB", "AI"], ["ML"]]}
        )

        self.assertTrue(onenormal_form(atomic))
        self.assertFalse(onenormal_form(non_atomic))

    def test_powerset_includes_empty_and_full_sets(self):
        subsets = list(powerset(["A", "B"]))

        self.assertEqual(subsets, [[], ["A"], ["B"], ["A", "B"]])


if __name__ == "__main__":
    unittest.main()
