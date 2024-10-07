def __main__():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        print_report(file_contents)

def count_words(book_text):
    words_split = book_text.split()
    return len(words_split)

def count_chars(book_text):
    letters = []

    for char in book_text:
        lower_char = char.lower()
        if lower_char.isalpha():
            found = False
            for d in letters:
                if d["character"] == lower_char:
                    found = True
                    d["occurrences"] += 1
                    break
            if not found:
                letters.append({"character": lower_char, "occurrences": 1})

    return letters

def sort_on_occurrences(dictionary):
    return dictionary["occurrences"]

def sort_on_alpha_order(dictionary):
    return dictionary["character"]

def print_report(book_text):
    # Begin Report
    print("--- Begin report of books/frankenstein.txt ---")

    # Printing amount of words
    num_words = count_words(book_text)
    print(f"{num_words} words found in the document\n")

    # Printing amount of each letter
    letter_dict = count_chars(book_text)
    # letter_dict.sort(reverse=False, key=sort_on_alpha_order) # Sorting letter by alphabet order
    letter_dict.sort(reverse=True, key=sort_on_occurrences) # Sorting letters by occurrence
    for dictionary in letter_dict:
        print(f"The '{dictionary["character"]}' character was found {dictionary["occurrences"]} times")

    # Ending Report
    print("--- End report ---")

__main__()
