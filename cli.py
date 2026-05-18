import argparse

# Commands: "add", "update", "delete", "summary", "list", "budget", "del_budget"

parser = argparse.ArgumentParser(
    prog="expense-tracker",
    description="A simple expense tracker application to manage your finances."
)

subparser = parser.add_subparsers(dest="command")

# 'add' command
add_parser = subparser.add_parser("add")
add_parser.add_argument("-d", "--description", type=str, required=True)
add_parser.add_argument("-a", "--amount", type=float, required=True)
add_parser.add_argument("-c", "--category", type=str)

# 'update' command
update_parser = subparser.add_parser("update")
update_parser.add_argument("--id", type=int, required=True)
update_parser.add_argument("-d", "--description", type=str)
update_parser.add_argument("-a", "--amount", type=float)
update_parser.add_argument("-c", "--category", type=str)

# 'delete' command
delete_parser = subparser.add_parser("delete")
delete_parser.add_argument("--id", type=int, required=True)

# 'summary' command
summary_parser = subparser.add_parser("summary")
summary_parser.add_argument("-d", "--date", type=str)

# 'list' command
list_parser = subparser.add_parser("list")
list_parser.add_argument("-f", "--filter", type=str)

# 'budget' command
budget_parser = subparser.add_parser("budget")
budget_parser.add_argument("-y", "--year", type=int, required=True)
budget_parser.add_argument("-m", "--month", type=int, required=True)
budget_parser.add_argument("-b", "--budget", type=float, required=True)

# 'del_budget' command
del_budget_parser = subparser.add_parser("del_budget")
del_budget_parser.add_argument("-y", "--year", type=int, required=True)
del_budget_parser.add_argument("-m", "--month", type=int, required=True)