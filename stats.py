def word_counter(file):
    split_file = file.split()
    return len(split_file)

def char_counter(file):
    char_counts = {}

    for i in file:
        char = i.lower()
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1

    return char_counts

def sort_on(items):
    return items["num"]

def sorted_report(file, filePath):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filePath}...")
    print("----------- Word Count ----------")
    print(f"Found {word_counter(file)} total words")
    print("--------- Character Count -------")

    unsorted_dic = char_counter(file)
    sorted_list = []
    for i in unsorted_dic:
        sorted_list.append({"char": i, "num": unsorted_dic[i]})

    sorted_list.sort(reverse=True, key=sort_on)

    for i in sorted_list:
        value = i["char"]
        if value.isalpha():
            print(f'{value}: {i["num"]}')
    
    print("============= END ===============")


