import sys


def nl(file_name: str):
    line_number = 1
    if file_name:
        try:
            with open(file_name, 'r') as file:
                for line in file:
                    print(f" {line_number}\t{line.rstrip()}")
                    line_number += 1
        except FileNotFoundError:
            print(f"nl: cannot open '{file_name}': No such file or directory")
    else:
        input_text = sys.stdin.read()
        lines = input_text.split('\n')
        for line in lines:
            print(f" {line_number}\t{line.rstrip()}")
            line_number += 1


if __name__ == "__main__":
    input_file = None
    if len(sys.argv) > 1:
        input_file = sys.argv[1]
    nl(input_file)
