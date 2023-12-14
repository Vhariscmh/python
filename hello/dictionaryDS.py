def construct_character_dict(word):
    # Create an empty dictionary to store character counts
    character_count_dict = dict()

    # Iterate through each character in the word
    for each_character in word:
        # Update the count for each character in the dictionary
        character_count_dict[each_character] = character_count_dict.get(each_character, 0) + 1

    # Sort the keys of the dictionary
    sorted_list_keys = sorted(character_count_dict.keys())

    # Print the characters and their counts in sorted order
    for each_key in sorted_list_keys:
        print(each_key, character_count_dict.get(each_key))

def main():
    # Take user input for a string
    word = input("Enter a string: ")

    # Call the function to construct and print the character dictionary
    construct_character_dict(word)

if __name__ == "__main__":
    main()
