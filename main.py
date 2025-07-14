import sys
from stats import get_num_words, count_characters

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    text = get_book_text(book_path)
    word_count = get_num_words(text)
    characters = count_characters(text)
    character_list = sort_data(characters)
    print_report(book_path, word_count, character_list)


def get_book_text(path):
    with open(path) as f:
        return f.read()


def sort_by_count(dict):
    return dict["count"]

def sort_data(dict):
    character_list = []
    for char, count in dict.items():
        if char.isalpha():
            new_dict = {"char": char, "count": count}
            character_list.append(new_dict)
    character_list.sort(reverse=True, key=sort_by_count)
    return character_list

def print_report(book, word_count, sorted_data):
    print(f"--- Begin report of {book} ---")
    print(f"{word_count} words found in the document")

    for item in sorted_data:
        print(f"{item['char']}: {item['count']}")

    print("--- End Report ---")    



   

main()




    
    