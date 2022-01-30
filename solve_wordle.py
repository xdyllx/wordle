def get_word_list_from_file(file_name):
    f = open(file_name)
    lines = f.readlines()
    words = list()
    for line in lines:
        words.append(line[:-1])

    return words


def select_word(words):
    char_count = dict()
    for word in words:
        for char in word:
            if char_count.get(char) is not None:
                char_count[char] += 1
            else:
                char_count[char] = 1

    for word in words:



def solve_wordle(answer):
    words = get_word_list_from_file('wordle_word.txt')
