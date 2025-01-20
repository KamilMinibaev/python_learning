#%% md
# ### Задание 5 - tf-idf vectorizer
#%%
from count_vectorizer import CountVectorizer
from tf_idf_transformer import TfidfTransformer
#%%
class TfidfVectorizer:
    def __init__(self):
        self.vectorizer = CountVectorizer()
        self.tfidf_transformer = TfidfTransformer()

    def fit_transform(self, corpus):

        count_matrix = self.vectorizer.fit_transform(corpus)

        # tf-idf преобразование
        tfidf_matrix = self.tfidf_transformer.fit_transform(count_matrix)

        return tfidf_matrix

    def get_feature_names(self):
        # Возвращаем список слов из CountVectorizer
        return self.vectorizer.get_feature_names()
#%%
corpus = [
    'Crock Pot Pasta Never boil pasta again',
    'Pasta Pomodoro Fresh ingredients Parmesan to taste'
]
#%%
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(corpus)

print(vectorizer.get_feature_names())
print(tfidf_matrix)