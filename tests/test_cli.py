import unittest
from cli import parser

class TestCli(unittest.TestCase):

    # add command tests
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


    # update command tests
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

    
    # delete command tests
    def test_delete_valid_args(self):
        args = parser.parse_args(["delete", "--id", "1"])
        self.assertEqual(args.command, "delete")
        self.assertEqual(args.id, 1)


    def test_delete_missing_id(self):
        with self.assertRaises(SystemExit):
            parser.parse_args(["delete"])


    # summary command tests
    def test_summary_valid_args(self):
        args = parser.parse_args(["summary", "--date", "2026-05"])
        self.assertEqual(args.command, "summary")
        self.assertEqual(args.date, "2026-05")


    def test_summary_missing_date(self):
        args = parser.parse_args(["summary"])
        self.assertEqual(args.command, "summary")
        self.assertIsNone(args.date)
    

    # list command tests
    def test_list_valid_args(self):
        args = parser.parse_args(["list", "--category", "Category"])
        self.assertEqual(args.command, "list")
        self.assertEqual(args.category, "Category")


    def test_list_missing_category(self):
        args = parser.parse_args(["list"])
        self.assertEqual(args.command, "list")
        self.assertIsNone(args.category)


    # set_budget command tests
    def test_set_budget_valid_args(self):
        args = parser.parse_args(["set_budget", "--date", "2026-05", "--amount", "500.50"])
        self.assertEqual(args.command, "set_budget")
        self.assertEqual(args.date, "2026-05")
        self.assertEqual(args.amount, 500.50)


    def test_set_budget_missing_date(self):
        with self.assertRaises(SystemExit):
            parser.parse_args(["budget", "--amount", "500.50"])


    def test_set_budget_wrong_budget_type(self):
        with self.assertRaises(SystemExit):
            parser.parse_args(["set_budget", "--date", "2026-05", "--bamount", "three-hundred"])


    # delete_budget command tests
    def test_delete_budget_valid_args(self):
        args = parser.parse_args(["delete_budget", "--date", "2026-05"])
        self.assertEqual(args.command, "delete_budget")
        self.assertEqual(args.date, "2026-05")


    def test_delete_budget_missing_date(self):
        with self.assertRaises(SystemExit):
            parser.parse_args(["delete_budget"])


    def test_delete_budget_wrong_date_type(self):
        with self.assertRaises(SystemExit):
            parser.parse_args(["del_budget", "--date", "two-thousand-twenty-six"])


    # view_budget command tests
    def test_view_budgets_valid_args(self):
        args = parser.parse_args(["view_budgets"])
        self.assertEqual(args.command, "view_budgets")


    def test_view_budgets_too_many_args(self):
        with self.assertRaises(SystemExit):
            parser.parse_args(["view_budgets", "--date", "2026-05"])


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