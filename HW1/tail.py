import sys


def tail(files: list[str]):
    def print_file_name(file_name: str):
        print(f"==> {file_name} <==")

    def print_last_lines(lines: list[str], n: int = 10):
        for line in lines[-n:]:
            print(line, end="")
        print("\n")

    if not files:
        lines = sys.stdin.readlines()
        print_file_name("stdin")
        print_last_lines(lines, n=17)
    else:
        for file_name in files:
            if len(files) > 1:
                print_file_name(file_name)
            try:
                with open(file_name, 'r') as file:
                    lines = file.readlines()
                    print_last_lines(lines)
            except FileNotFoundError:
                print(f"tail: cannot open '{file_name}': No such file or directory")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        files = sys.argv[1:]
        tail(files)
    else:
        tail([])
