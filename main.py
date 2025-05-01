import argparse
from calculator import Calculator
from function import greet_user

def main():

    parser = argparse.ArgumentParser(description='Simple CLI command')
    subparsers = parser.add_subparsers(dest="command", required=True)

    #add command
    add_parser = subparsers.add_parser("add", help="add two numbers")
    add_parser.add_argument("a", type=float)
    add_parser.add_argument("b", type=float)

    #multiply command
    mul_parser = subparsers.add_parser("multiply", help="multiply two numbers")
    mul_parser.add_argument("a", type=float)
    mul_parser.add_argument("b", type=float)

    #greet command
    greet_parser = subparsers.add_parser("greet", help="greet a user")
    greet_parser.add_argument("name", type=str)

    args = parser.parse_args()
    calc = Calculator()

    if args.command == "add":
        print(f"Result: {calc.add(args.a, args.b)}")
    elif args.command == "multiply":
        print(f"Result: {calc.multiply(args.a, args.b)}")
    elif args.command == "greet":
        print(greet_user(args.name))

if __name__ == "__main__":
    main()