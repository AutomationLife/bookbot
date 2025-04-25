def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

def word_count(file_contents):
    words = file_contents.split()
    return len(words)

def char_count(file_contents):
    count= {}
    new_file_contents = file_contents.lower()
    for char in new_file_contents:
        if char in count:
            count[char] += 1
        else:
            count[char] = 1
    return count

def sort_char_count(char_count_result):
    sorted_count = sorted(char_count_result.items(), key=lambda x: x[1], reverse=True)
    return sorted_count