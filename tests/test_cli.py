import unittest
from cli import parser

class TestCli(unittest.TestCase):

    # Add command tests
    def test_add_valid_args(self):
        args = parser.parse_args(["add", "--description", "Netflix", "--amount", "21.99", "--category", "Entertainment"])
        self.assertEqual(args.command, "add")
        self.assertEqual(args.description, "Netflix")
        self.assertEqual(args.amount, 21.99)
        self.assertEqual(args.category, "Entertainment")

    def test_add_missing_amount(self):
        with self.assertRaises(SystemExit):
            parser.parse_args(["add", "--description", "Netflix"])

    def test_add_missing_description(self):
        with self.assertRaises(SystemExit):
            parser.parse_args(["add", "--amount", "21.99"])

    def test_add_wrong_type(self):
        with self.assertRaises(SystemExit):
            parser.parse_args(["add", "--description", "Netflix", "--amount", "twenty"])


    # Update command tests
    def test_update_valid_args(self):
        args = parser.parse_args(["update", "--id", "1", "--description", "Netflix", "--amount", "21.99", "--category", "Entertainment"])
        self.assertEqual(args.command, "update")
        self.assertEqual(args.id, 1)
        self.assertEqual(args.description, "Netflix")
        self.assertEqual(args.amount, 21.99)
        self.assertEqual(args.category, "Entertainment")
    
    def test_update_missing_id(self):
        with self.assertRaises(SystemExit):
            parser.parse_args(["update", "--description", "Netflix", "--amount", "21.99", "--category", "Entertainment"])

    
    # Delete command tests
    def test_delete_valid_args(self):
        args = parser.parse_args(["delete", "--id", "1"])
        self.assertEqual(args.command, "delete")
        self.assertEqual(args.id, 1)

    def test_delete_missing_id(self):
        with self.assertRaises(SystemExit):
            parser.parse_args(["delete"])

    # Summary command tests
    def test_summary_valid_args(self):
        args = parser.parse_args(["summary", "--date", "2026-05"])
        self.assertEqual(args.command, "summary")
        self.assertEqual(args.date, "2026-05")

    def test_summary_missing_date(self):
        args = parser.parse_args(["summary"])
        self.assertEqual(args.command, "summary")
        self.assertIsNone(args.date)

    
    # List command tests
    def test_list_valid_args(self):
        args = parser.parse_args(["list", "--filter", "Category"])
        self.assertEqual(args.command, "list")
        self.assertEqual(args.filter, "Category")

    def test_list_missing_filter(self):
        args = parser.parse_args(["list"])
        self.assertEqual(args.command, "list")
        self.assertIsNone(args.filter)


    # Budget command tests
    def test_budget_valid_args(self):
        args = parser.parse_args(["budget", "--year", "2026", "--month", "5", "--budget", "500.50"])
        self.assertEqual(args.command, "budget")
        self.assertEqual(args.year, 2026)
        self.assertEqual(args.month, 5)
        self.assertEqual(args.budget, 500.50)

    def test_budget_missing_year(self):
        with self.assertRaises(SystemExit):
            parser.parse_args(["budget", "--month", "5", "--budget", "500.50"])

    def test_budget_wrong_budget_type(self):
        with self.assertRaises(SystemExit):
            parser.parse_args(["budget", "--year", "2026", "--month", "5", "--budget", "three-hundred"])


    # Del_budget command tests
    def test_del_budget_valid_args(self):
        args = parser.parse_args(["del_budget", "--year", "2026", "--month", "06"])
        self.assertEqual(args.command, "del_budget")
        self.assertEqual(args.year, 2026)
        self.assertEqual(args.month, 6)

    def test_del_budget_missing_month(self):
        with self.assertRaises(SystemExit):
            parser.parse_args(["del_budget", "--year", "2026"])

    def test_del_budget_missing_year(self):
        with self.assertRaises(SystemExit):
            parser.parse_args(["del_budget", "--month", "12"])

    def test_del_budget_wrong_year_type(self):
        with self.assertRaises(SystemExit):
            parser.parse_args(["del_budget", "--year", "two-thousand-twenty-six", "--month", "06"])


    # Test unrecognised command
    def test_unrecognised_command(self):
        with self.assertRaises(SystemExit):
            parser.parse_args(["random_command"])


    # Test empty args
    def test_empty_args(self):
        args = parser.parse_args([])
        self.assertIsNone(args.command)

if __name__ == "__main__":
    unittest.main()