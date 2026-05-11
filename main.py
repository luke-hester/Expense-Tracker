from cli import parser

def main():
    args = parser.parse_args()
    print(args)

    if args.command == "add":
        print(f"Added new expense {args.description}, €{args.amount} per month")

if __name__ == "__main__":
    main()