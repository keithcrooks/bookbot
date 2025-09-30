def get_character_frequency(text):
    characters = {}

    lower_case_text = text.lower()

    for char in lower_case_text:
        if char not in characters:
            characters[char] = 1
            continue

        characters[char] += 1

    return characters

def sort_by_count(items):
    return items["count"]

def get_characters_sorted_by_frequency(characters):
    character_list = []

    for char in characters:
        character_list.append({"char": char, "count": characters[char]})

    character_list.sort(reverse=True, key=sort_by_count)

    return character_list

def get_num_words(text):
    words = text.split()
    return len(words)
