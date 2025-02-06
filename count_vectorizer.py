import math
from typing import List, Tuple, Optional
# например, optional[int] выдает int или none

# Задание 1 - count vectorizer
class CountVectorizer:
    def __init__(self):
        self.word_count = {}

    def fit(self, corpus):
        self.word_count = {}

        for sentence in corpus:
            # чтобы на регистр не обращать внимания
            sentence = sentence.lower()

            # делим предложения на слова по пробелам
            sentence = sentence.split(' ')

            for word in sentence:
                # считаем кол-во повторений слов
                self.word_count[word] = self.word_count.get(word, 0) + 1

        return self.word_count

    def transform(self, corpus:list[str]) -> list[list[int]]:
        count_matrix = []

        for sentence in corpus:
            word_list = self.get_feature_names()

            sentence_word_count = {}
            # чтобы на регистр не обращать внимания
            sentence = sentence.lower()

            # делим предложения на слова по пробелам
            sentence = sentence.split(' ')

            for word in sentence:
                # считаем кол-во повторений слов в конкретном предложении
                sentence_word_count[word] = sentence_word_count.get(word, 0) + 1

            word_count_sentence = []
            for word in word_list:
                current_word_count = sentence_word_count.get(word, 0)

                word_count_sentence.append(current_word_count)

            count_matrix.append(word_count_sentence)

        return count_matrix

    def get_feature_names(self) -> Optional[List[str]]:

        word_order = list(self.word_count.keys())

        return word_order

    def fit_transform(self, corpus):
        self.fit(corpus)

        return self.transform(corpus)

# Задание 2 - term frequency
def tf_transform(count_matrix):
    word_freq = []
    for sentence in count_matrix:
        sentence_word_freq = []
        sentence_word_count = sum(sentence)

        for word in sentence:
            cur_word_freq = round(word / sentence_word_count, 3)

            sentence_word_freq.append(cur_word_freq)

        word_freq.append(sentence_word_freq)

    return word_freq

# Задание 3 - inverse document-frequency
def step_function(number):
    return 1 if number >= 1 else 0

def idf_transform(count_matrix):
    doc_amount = len(count_matrix)

    column_sum = []

    for j in range(len(count_matrix[0])):
        element_sum = 0

        for i in range(doc_amount):
            element_sum += step_function(count_matrix[i][j])

        element_idf = round(math.log( (doc_amount + 1) / (element_sum + 1))+ 1, 3)
        column_sum.append(element_idf)

    return column_sum

if __name__ == '__main__':
    # сначала CountVectorizer
    vectorizer = CountVectorizer()

    corpus = [
        'Crock Pot Pasta Never boil pasta again',
        'Pasta Pomodoro Fresh ingredients Parmesan to taste'
    ]

    count_matrix = vectorizer.fit_transform(corpus)
    print(count_matrix)

    print(vectorizer.get_feature_names())

    # теперь TF-трансформация
    tf_matrix = tf_transform(count_matrix)
    print(tf_matrix)

    # финально IDF-трансформация

    idf_matrix = idf_transform(count_matrix)
    print(idf_matrix)