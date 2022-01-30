def gen_words_of_length_five(input_file_name, output_file_name='word5.txt'):
    f = open(input_file_name)
    lines = f.readlines()
    result_lines = list()
    for line in lines:
        line = line.lower()
        if is_valid_word(line[:-1]):
            result_lines.append(line)

    result_lines = list(set(result_lines))
    result_lines.sort()
    result_file = open(output_file_name, 'w+')
    result_file.writelines(result_lines)
    f.close()
    result_file.close()


def is_valid_word(word):
    if len(word) != 5:
        return False
    for char in word:
        if char < 'a' or char > 'z':
            return False
    return True


if __name__ == '__main__':


    gen_words_of_length_five('word.txt', 'word5.txt')