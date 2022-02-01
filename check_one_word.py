from solve_wordle import solve_wordle, get_word_list_from_file

if __name__ == '__main__':
    total_words = get_word_list_from_file('wordle_word.txt')
    solve_wordle(total_words, 'daddy', True)
