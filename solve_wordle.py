from enum import Enum
import numpy as np
from select_word_function import *

DEBUG_MODE = False
SELECT_WORD_FUNCTION = select_word


def debug_print(sth):
    if DEBUG_MODE:
        print(sth)


class RuleType(Enum):
    UNKNOWN = 0
    CORRECT = 1
    EXIST = 2
    NOT_EXIST = 3


class Rule:
    # 如果type是CORRECT, pos表示word正确的位置
    # 如果type是EXIST， 表示char存在但不在pos这个位置
    def __init__(self, char, rule_type, pos=-1):
        self.char = char
        self.rule_type = rule_type
        self.pos = pos

    def __str__(self):
        return '{' + str(self.rule_type) + ', ' + self.char + ' ' + str(self.pos) + '}'

    def pass_check(self, word):
        if self.rule_type == RuleType.CORRECT:
            return word[self.pos] == self.char
        elif self.rule_type == RuleType.EXIST:
            return (self.char in word) and (word[self.pos] != self.char)
        elif self.rule_type == RuleType.NOT_EXIST:
            return self.char not in word
        else:
            raise Exception('invalid rule')


def get_word_list_from_file(file_name):
    f = open(file_name)
    lines = f.readlines()
    words = list()
    for line in lines:
        words.append(line[:-1])

    return words


def gen_word_rules(word, answer):
    rules = list()
    for i in range(5):
        if word[i] == answer[i]:
            rules.append(Rule(word[i], RuleType.CORRECT, i))
        elif word[i] in answer:
            rules.append(Rule(word[i], RuleType.EXIST, i))
        else:
            rules.append(Rule(word[i], RuleType.NOT_EXIST))
    return rules


def filter_words_by_rules(words, rules):
    result_words = list()
    for word in words:
        pass_rule_check = True
        for rule in rules:
            if not rule.pass_check(word):
                pass_rule_check = False
                break
        if pass_rule_check:
            result_words.append(word)
    return result_words


def solve_wordle(words, answer, debug=False):
    global DEBUG_MODE
    if debug:
        DEBUG_MODE = True
    count = 0
    while (True):
        count += 1
        if len(words) <= 0:
            raise Exception('words length = 0')
        word = SELECT_WORD_FUNCTION(words)
        debug_print(f'count:{count}, select word:{word}')
        if word == answer:
            break

        rules = gen_word_rules(word, answer)
        words = filter_words_by_rules(words, rules)
        debug_print(f'count:{count}, result words(len={len(words)}):{words}')

    debug_print(f'answer:{answer}, final count:{count}')
    return count


if __name__ == '__main__':

    total_words = get_word_list_from_file('wordle_word.txt')


    word_count_map = dict()
    for word in total_words:
        count = solve_wordle(total_words, word)
        word_count_map[word] = count

    avg = np.average(list(word_count_map.values()))
    print(f'avg={avg}')

    sort_result = sorted(word_count_map.items(), key=lambda kv: kv[1], reverse=True)
    failed_result = list()
    for result in sort_result:
        if result[1] > 6:
            failed_result.append(result)
    print(f'failed_result(length={len(failed_result)}):{failed_result}')
    print(sort_result)
