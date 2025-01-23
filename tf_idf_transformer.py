import math

def step_function(number):
    return 1 if number >= 1 else 0

# Задание 4 - tf-idf transformer
class TfidfTransformer:

    @staticmethod
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

    @staticmethod
    def idf_transform(count_matrix):
        doc_amount = len(count_matrix)

        column_sum = []

        for j in range(len(count_matrix[0])):
            element_sum = 0

            for i in range(doc_amount):
                element_sum += step_function(count_matrix[i][j])

            element_idf = round(math.log((doc_amount + 1) / (element_sum + 1)) + 1, 3)
            column_sum.append(element_idf)

        return column_sum

    @staticmethod
    def fit_transform(count_matrix):

        tf_transform_result = TfidfTransformer.tf_transform(count_matrix)
        idf_transform_result = TfidfTransformer.idf_transform(count_matrix)

        # завожу пустой список из списков, количество которых равно количеству списков после выполнения tf_transform
        result = [[] for _ in range(len(tf_transform_result))]

        for n in range(len(tf_transform_result)):
            every_list = tf_transform_result[n]
            for i in range(len(every_list)):
                result_item = round(every_list[i] * idf_transform_result[i], 3)
                result[n].append(result_item)

        return result

if __name__ == '__main__':
    count_matrix = [
    [1, 1, 2, 1, 1, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1]]

    tfidf_matrix = TfidfTransformer.fit_transform(count_matrix)
    print(tfidf_matrix)