def find_even_numbers(item_list):
    print("The EVEN numbers in the list are:")
    for item in item_list:
        if item % 2 == 0:
            print(item)

def main():
    list1 = [2, 3, 6, 8, 48, 97, 56]
    find_even_numbers(list1)

if __name__ == "__main__":
    main()
