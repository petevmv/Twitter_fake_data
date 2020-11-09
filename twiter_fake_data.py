def strip_punctuation(x):
    for word in x:
        for ch in word:
            for punct in punctuation_chars:
                if punct == ch:
                    x = x.replace(ch, "")

    return x

def count_words(y, list_of_words):
    y = strip_punctuation(y).lower()
    counter = 0
    for word in y.split():
        for sub_word in list_of_words:
            if word == sub_word:
                counter += 1
    return counter


def get_pos(y):
    return count_words(y, positive_words)

def get_neg(y):
    return count_words(y, negative_words)
# def get_pos(y):
#     y = strip_punctuation(y)
#     positive_word_count = 0
#     y_lower = y.lower()
#
#     for word in y_lower.split():
#         for pos_word in positive_words:
#             if word == pos_word:
#                 positive_word_count += 1
#     return positive_word_count
#
# def get_neg(y):
#     y = strip_punctuation(y)
#     neg_word_count = 0
#     y_lower = y.lower()
#
#     for word in y_lower.split():
#         #print(word)
#         for neg_word in negative_words:
#             if word == neg_word:
#                 neg_word_count += 1
#     return neg_word_count


punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
# lists of words to use
positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())



negative_words = []
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())


handle_file = open("project_twitter_data.txt")
lines = handle_file.readlines()

text = handle_file.read()
text_for_net_score = text.strip().split(',')

positive = get_pos(text)
negative = get_neg(text)

net_s = positive - negative



outfile = open("resulting_data.csv", "w")
outfile.write("Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score")
outfile.write("\n")
for linz in lines[1:]:

    clean_lines = linz.strip().split(',')
    net_s = get_pos(linz) - get_neg(linz)
    print(clean_lines)
    row_string = '{},{},{},{},{}'.format(clean_lines[1], clean_lines[2], positive, negative, net_s)
    outfile.write(row_string)
    outfile.write('\n')

outfile.close()
