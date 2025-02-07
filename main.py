def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = count_words(text)
    characters = count_characters(text)
    character_list = sort_data(characters)
    print_report(book_path, word_count, character_list)


def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_words(text):
    words = text.split()
    count = 0
    for word in words:
        count += 1
    return count    

def count_characters(text):
    lower_case = text.lower()
    character_count = {}
    for char in lower_case:
        if char in character_count:
            character_count[char] += 1
        else:
            character_count[char] = 1
    return character_count

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
        print(f"The '{item['char']}' character was found {item['count']} times")

    print("--- End Report ---")    



        
   
   

main()




    
    