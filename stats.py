def get_num_words(text):
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