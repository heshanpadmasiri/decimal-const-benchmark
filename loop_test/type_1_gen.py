import random
import decimal
import sys

decimal.setcontext(decimal.ExtendedContext);

INDENT = "    "

def gen_random_num():
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
    return [decimal.Decimal(value), value]

def gen_main(file, m):
    print(f"\t {file.name} main start")
    file.write("public function main() {\n")
    file.write(f'{INDENT}decimal[] values = [')
    for i, _ in enumerate(range(m)):
        if i > 0:
            file.write(", ")
        file.write(gen_random_num()[1])
    file.write('];\n')
    file.write(INDENT + 'foreach int index in 0 ..< values.length() {\n')
    file.write(INDENT * 2 + 'io:println(group(values[index]));\n')
    file.write(INDENT + '}\n')
    file.write('}')
    print(f"\t {file.name} main done")

def gen_condition(i, val):
    body = [];
    if i == 0:
        body.append(f'{INDENT}if val > {val}d {{\n');
    else:
        body.append(f'{INDENT}else if val > {val}d {{\n');
    body.append(f'{INDENT*2}return {i};\n')
    body.append(f'{INDENT}}}\n')
    return body

def gen_group(file, n):
    print(f"\t {file.name} group start")
    print(f"\t {file.name} value gen start")
    values = list(map(lambda value: value[1], sorted([gen_random_num() for _ in range(n)], reverse=True)))
    print(f"\t {file.name} value gen done")
    file.write("function group(decimal val) returns int {\n")
    for i in range(len(values)):
        file.writelines(gen_condition(i, values.pop()))
    file.write(f'{INDENT}return {n};\n')
    file.write(f'}}\n')
    print(f"\t {file.name} group done")

def gen_test(output_file_name, n, m):
    print(f'{output_file_name} start')
    with open(output_file_name, "w", buffering=int(1E9)) as file:
        file.write("import ballerina/io;\n\n")
        gen_main(file, n)
        file.write("\n")
        gen_group(file, m)
    print(f'{output_file_name} done')
    return 0

def gen_type_1_test(output_file_name, n, m):
    gen_test(output_file_name, int(n), int(m))

if __name__ == "__main__":
    output_file_name = sys.argv[1]
    n, m = map(lambda x: 10**(int(x)), sys.argv[2:])
    gen_test(output_file_name, n, m)
