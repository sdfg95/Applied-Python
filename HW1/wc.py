import sys


def wc(files: list[str]):
    total_lines = 0
    total_words = 0
    total_bytes = 0

    def count_stats(file_name: str, lines: int, words: int, bytes: int):
        print(f"\t{lines}\t{words}\t{bytes}\t{file_name}")

    if not files:
        input_text = sys.stdin.read()
        lines = input_text.split('\n')
        words = sum(len(line.split()) for line in lines)
        bytes = len(input_text.encode('utf-8'))
        print(f"\n\t{len(lines)}\t{words}\t{bytes}")
    else:
        for file in files:
            try:
                with open(file, 'r') as f:
                    lines = 0
                    words = 0
                    bytes = 0

                    for line in f:
                        lines += 1
                        words += len(line.split())
                        bytes += len(line.encode('utf-8'))

                    count_stats(file, lines, words, bytes)

                    total_lines += lines
                    total_words += words
                    total_bytes += bytes

            except FileNotFoundError:
                print(f"wc: {file}: No such file or directory")

        if len(files) > 1:
            count_stats("total", total_lines, total_words, total_bytes)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        files = sys.argv[1:]
        wc(files)
    else:
        wc([])
