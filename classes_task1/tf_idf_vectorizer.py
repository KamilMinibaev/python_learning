# Задание 5 - tf-idf vectorizer

from count_vectorizer import CountVectorizer
from tf_idf_transformer import TfidfTransformer

class TfidfVectorizer(CountVectorizer):

    def __init__(self):

        self.tfidf_transformer = TfidfTransformer()

        # так как наследуемся, то необязательно инициализировать CountVectorizer
        super().__init__()

    def fit_transform(self, corpus):

        # так как наследуемся, то необязательно прописывать CountVectorizer, можно через super вызывать метод родителя
        count_matrix = super().fit_transform(corpus)

        # tf-idf преобразование
        tfidf_matrix = self.tfidf_transformer.fit_transform(count_matrix)

        return tfidf_matrix

if __name__ == '__main__':
    corpus = [
        'Crock Pot Pasta Never boil pasta again',
        'Pasta Pomodoro Fresh ingredients Parmesan to taste'
    ]

    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(corpus)

    print(vectorizer.get_feature_names())
    print(tfidf_matrix)