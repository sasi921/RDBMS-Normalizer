import unittest

import pandas as pd

from data_parser import data_parser


class DataParserTests(unittest.TestCase):
    def test_splits_and_trims_comma_separated_values(self):
        frame = pd.DataFrame({
            "skills": ["SQL, Python", "Java"],
            "name": ["Ada", "Grace"],
        })

        parsed = data_parser(frame.copy())

        self.assertEqual(parsed.loc[0, "skills"], ["SQL", "Python"])
        self.assertEqual(parsed.loc[1, "skills"], ["Java"])
        self.assertEqual(parsed["name"].tolist(), ["Ada", "Grace"])

    def test_converts_scalar_values_to_strings(self):
        frame = pd.DataFrame({"id": [101, 202]})

        parsed = data_parser(frame.copy())

        self.assertEqual(parsed["id"].tolist(), ["101", "202"])

    def test_leaves_columns_without_commas_as_scalar_strings(self):
        frame = pd.DataFrame({"city": ["Rolla", "Austin"]})

        parsed = data_parser(frame.copy())

        self.assertEqual(parsed["city"].tolist(), ["Rolla", "Austin"])
        self.assertTrue(all(isinstance(value, str) for value in parsed["city"]))


if __name__ == "__main__":
    unittest.main()
