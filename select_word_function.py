def select_word(words):
    if len(words) == 1:
        return words[0]
    char_count = dict()
    total_char_count = 5 * len(words)
    for word in words:
        for char in word:
            if char_count.get(char) is not None:
                char_count[char] += 1
            else:
                char_count[char] = 1
    word_score_list = list()
    for word in words:
        dedeplicate_char_set = set(word)
        score = 0
        for char in dedeplicate_char_set:
            score += char_count[char]
        word_score_list.append({'word': word, 'score': score})
    word_score_list = sorted(word_score_list, key=lambda x: x['score'], reverse=True)
    return word_score_list[0]['word']


# worse
def select_word2(words):
    if len(words) == 1:
        return words[0]
    char_count = dict()

    # char_pos_count[i][j] 表示字符为i在第j位出现的次数
    char_pos_count = dict()

    for word in words:
        for i in range(5):
            char = word[i]
            if char_count.get(char) is not None:
                char_count[char] += 1
            else:
                char_count[char] = 1

            pos_count = char_pos_count.get(char)
            if pos_count is not None:
                pos_count[i] += 1
            else:
                char_pos_count[char] = [0,0,0,0,0]
                char_pos_count[char][i] += 1

    word_score_list = list()
    for word in words:
        dedeplicate_char_set = set()
        score = 0
        for i in range(5):
            char = word[i]
            if char in dedeplicate_char_set:
                score += char_count[char] * 0.1 * char_pos_count[char][i]
            else:
                score += char_count[char] * (0.9 + 0.1 * char_pos_count[char][i])
                dedeplicate_char_set.add(char)
        word_score_list.append({'word': word, 'score': score})
    word_score_list = sorted(word_score_list, key=lambda x: x['score'], reverse=True)
    return word_score_list[0]['word']
