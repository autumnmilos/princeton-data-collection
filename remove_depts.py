def remove_line_after_empty_line(input_filename, output_filename):
    with open(input_filename, 'r') as infile:
        lines = infile.readlines()

    output_lines = []
    skip_line = False
    for line in lines:
        if line.strip() == '':
            skip_line = True
        elif skip_line:
            skip_line = False
            continue
        output_lines.append(line)

    with open(output_filename, 'w') as outfile:
        outfile.writelines(output_lines)

if __name__ == '__main__':
    input_filename = 'output.txt'  # Replace with your input file name
    output_filename = 'output2.txt'  # Replace with your output file name
    remove_line_after_empty_line(input_filename, output_filename)
    print("Lines removed successfully.")
