from stats import word_counter, char_counter, sorted_report
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
else:
    sorted_report(get_book_text(sys.argv[1]), sys.argv[1])