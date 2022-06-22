import type_1_gen
from multiprocessing import Process

def gen_type_1(input_file):
    lines = []
    with open(input_file) as file:
        lines = file.readlines();
    threads = []
    for line in lines:
        n, m = map(int, line.strip().split())
        file_name = f'loop_1_{n:06}_{m}.bal'
        thread = Process(target=type_1_gen.gen_type_1_test, args=(file_name, n, m))
        thread.start()
        threads.append(thread)
    for thread in threads:
        thread.join()

if __name__ == "__main__":
    gen_type_1("values.txt")
