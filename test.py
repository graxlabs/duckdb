import unittest
from query import query, queryFromFile


class TestMain(unittest.TestCase):
    def test_query_csv(self):
        out = query("SELECT Id FROM Account.csv LIMIT 1").fetchall()
        self.assertEqual(out, [("0014600000VpLa3AAF",)])

    def test_query(self):
        out = query("SELECT 1").fetchall()
        self.assertEqual(out, [(1,)])

    def test_main(self):
        self.assertTrue(True)


if __name__ == "__main__":
    unittest.main()
