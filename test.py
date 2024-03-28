import unittest
from query import query, queryFile


class TestMain(unittest.TestCase):
    def test_query(self):
        out = query("SELECT 1").fetchall()
        self.assertEqual(out, [(1,)])

    def test_query_csv(self):
        out = query("SELECT Id FROM Account.csv LIMIT 1").fetchall()
        self.assertEqual(1, len(out))

    def test_query_file(self):
        out = queryFile("sql/Count.sql").fetchall()
        self.assertEqual(1, len(out))


if __name__ == "__main__":
    unittest.main()
