from decimal import *
import sys
import testGen
import random
import argparse
from tqdm import tqdm

T = 34
DEFAULT_RANGE = {
    "int": [Decimal("9"*T) * -1, Decimal("9"*T)]
}

def gen_random_test_int(output_file, N, n_min, n_max):
    vals = []
    for _ in tqdm(range(N)):
        vals.append(random.randint(n_min, n_max))
    print("values generated")
    testGen.output_gen(output_file, map(str, vals))

def gen_random_test(output_file, N):
    vals = []
    for _ in tqdm(range(N)):
        digits = str(random.randint(0, int("9"*34)))
        n_digits = len(digits)
        sign = random.choice(["", "-"])
        dot_pos = random.randint(0, n_digits)
        exponent = random.choice([0, random.randint(-6176, 6111)]) # force higher number of 0's
        value = sign
        if dot_pos != 0:
            value += digits[:dot_pos] + "." + digits[dot_pos:]
            value = value.strip(".")
        else:
            value += digits
        if exponent != 0:
            value += "E" + str(exponent)
        vals.append(value)
    testGen.output_gen(output_file, vals)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='generate random test cases for ballerina decimal')
    parser.add_argument('output', type=str, help='output filename')
    parser.add_argument('N', type=int, help='number of test cases')
    parser.add_argument('type', type=int, help='1: int')
    parser.add_argument('-n_min', type=str, help='minimum value for test case')
    parser.add_argument('-n_max', type=str, help='maximum value for test case')
    args = parser.parse_args()
    if args.type == 1:
        n_min = int(args.n_min) if args.n_min else DEFAULT_RANGE['int'][0]
        n_max = int(args.n_max) if args.n_max else DEFAULT_RANGE['int'][1]
        gen_random_test_int(args.output, args.N, n_min, n_max)
    elif args.type == 2:
        gen_random_test(args.output, args.N)
    else:
        print("only int tests implemented")