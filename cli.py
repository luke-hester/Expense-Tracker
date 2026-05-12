import argparse

# Commands: "add", "update", "delete", "summary", "list", "help"

parser = argparse.ArgumentParser(
    prog="expense-tracker",
    description="A simple expense tracker application to manage your finances."
)

subparser = parser.add_subparsers(dest="command")

# 'add' command
add_parser = subparser.add_parser("add")
add_parser.add_argument("-d", "--description", type=str, required=True)
add_parser.add_argument("-a", "--amount", type=float, required=True)

# 'update' command
update_parser = subparser.add_parser("update")
update_parser.add_argument("--id", type=int, required=True)
update_parser.add_argument("-d", "--description", type=str)
update_parser.add_argument("-a", "--amount", type=float)

# 'delete' command
delete_parser = subparser.add_parser("delete")
delete_parser.add_argument("--id", type=int, required=True)

# 'summary' command
summary_parser = subparser.add_parser("summary")

# 'list' command
list_parser = subparser.add_parser("list")