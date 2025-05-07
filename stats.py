def get_word_count(text):
    words = text.split()
    return len(words)

def get_chars_dict(text):
    chars_dict = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars_dict:
            chars_dict[lowered] += 1
        else:
            chars_dict[lowered] = 1
    return chars_dict

def sort_on(d):
    return d["num"]

def get_chars_list(dict):
    sorted_chars_list = []
    for item in dict:
        sorted_chars_list.append({"char": item, "num": dict[item]})
        sorted_chars_list.sort(reverse=True, key=sort_on)
    return sorted_chars_list
