# import sys

# if len(sys.argv) == 1:
#     print("meow")
# elif len(sys.argv) == 3 and sys.argv[1]=='-n':
#     n=int(sys.argv[2])
#     for _ in range(n):
#         print("meow")
# else:
#     print("usage of meow_19.py")

# what if if the input contains more -n, -a, -b, -d for different representation

import argparse

parser=argparse.ArgumentParser(description='Meow like a cat')
parser.add_argument('-n',default=1, help='no. of times to meow', type=int)
args=parser.parse_args()

print(type(args))

for _ in range(args.n):
    print("meow")

