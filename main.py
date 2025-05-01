import argparse

parser = argparse.ArgumentParser(description='Hello world')

text = parser.add_argument('hello', nargs=2, type=str, help='Greet user')

args = parser.parse_args()

print(args.hello)