import sys
def get_output_line(index, value):
    var_name = f'v_{index}'
    lines = [f'decimal {var_name} = {value};\n', f'io:println({var_name});\n']
    return list(map(lambda line: "    " + line, lines))

def output_gen(output_file_name, values):
    with open(output_file_name, 'w') as file:
        file.write("import ballerina/io;\n\n");
        file.write("public function main() {\n");
        for index, value in enumerate(values):
            file.writelines(get_output_line(index, value))
        file.write("}\n");


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("expect filename value+")
        sys.exit(1);
    output_file_name = sys.argv[1];
    values = sys.argv[2:]
    output_gen(output_file_name, values)