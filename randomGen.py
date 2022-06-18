from decimal import *
import sys
import testGen
import random
import argparse

T = 50
DEFAULT_RANGE = {
    "int": [Decimal("9"*T) * -1, Decimal("9"*T)]
}

def gen_random_test_int(output_file, N, n_min, n_max):
    vals = [random.randint(n_min, n_max) for _ in range(N)]
    testGen.output_gen(output_file, map(str, vals))


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
    else:
        print("only int tests implemented")