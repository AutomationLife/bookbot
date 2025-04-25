import sys
from stats import word_count, get_book_text, char_count, sort_char_count

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    file_path = sys.argv[1]
    book_text = get_book_text(file_path)
    word_count_result = word_count(book_text)
    char_count_result = char_count(book_text)
    sorted_char_count_result = sort_char_count(char_count_result)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count_result} total words")
    print("----------- Character Count -----")
    for char, count in sorted_char_count_result:
        if char.isalpha():
            print(f"{char}: {count}")
    print("============= END ===============")
main()