#%% md
# ## TF - IDF
#%% md
# ### Задание 1 - count vectorizer
#%%
class CountVectorizer:
    def __init__(self, word_count=None):
        self.word_count = word_count

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

    def get_feature_names(self):
        word_order = list(self.word_count.keys())

        return word_order

    def transform(self, corpus):
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

            for word in word_list:
                current_word_count = sentence_word_count.get(word, 0)
                word_list = list(map(lambda x: x.replace(word, str(current_word_count)), word_list))

            count_matrix.append(word_list)

        return count_matrix

    def fit_transform(self, corpus):
        self.fit(corpus)

        return self.transform(corpus)
#%%
vectorizer = CountVectorizer()
#%%
corpus = [
    'Crock Pot Pasta Never boil pasta again',
    'Pasta Pomodoro Fresh ingredients Parmesan to taste'
]
#%%
count_matrix = vectorizer.fit_transform(corpus)
count_matrix
#%%
print(vectorizer.get_feature_names())
#%% md
# ### Задание 2 - term frequency
#%%
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
#%%
count_matrix = [
    [1, 1, 2, 1, 1, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1]
]
#%%
tf_matrix = tf_transform(count_matrix)
print(tf_matrix)