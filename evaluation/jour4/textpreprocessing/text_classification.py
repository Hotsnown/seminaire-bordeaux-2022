from nbautoeval import ExerciseFunction, Args
from nbautoeval import CallRenderer, PPrintRenderer
import random

from sklearn.feature_extraction.text import CountVectorizer
import numpy as np
import pandas as pd

#BAG OF WORDS

def count_vectorizer(norm_corpus):
    cv = CountVectorizer(min_df=0., max_df=1.)
    return cv.fit_transform(norm_corpus)

arguments = [
    Args(['The sky is blue and beautiful.' 'Love this blue and beautiful sky!']),
    Args(['The quick brown fox jumps over the lazy dog.']),
    Args(["A king's breakfast has sausages, ham, bacon, eggs, toast and beans"]),
    Args(['I love green eggs, ham, sausages and bacon!']),
    Args(['The brown fox is quick and the blue dog is lazy!']),
    Args(['The sky is very blue and the sky is very beautiful today']),
    Args(['The dog is lazy but the brown fox is quick!']),
]

exo_count_vectorizer = ExerciseFunction(
    count_vectorizer,
    arguments
)

def dense_representation(norm_corpus):
    # get all unique words in the corpus
    cv = CountVectorizer(min_df=0., max_df=1.)
    cv_matrix = cv.fit_transform(norm_corpus)
    # show document feature vectors
    return cv_matrix.toarray()

arguments = [
    Args(count_vectorizer('The sky is blue and beautiful.' 'Love this blue and beautiful sky!')),
    Args(count_vectorizer('The quick brown fox jumps over the lazy dog.')),
    Args(count_vectorizer("A king's breakfast has sausages, ham, bacon, eggs, toast and beans")),
    Args(count_vectorizer('I love green eggs, ham, sausages and bacon!')),
    Args(count_vectorizer('The brown fox is quick and the blue dog is lazy!')),
    Args(count_vectorizer('The sky is very blue and the sky is very beautiful today')),
    Args(count_vectorizer('The dog is lazy but the brown fox is quick!')),
]

exo_dense_representation = ExerciseFunction(
    dense_representation,
    arguments
)

def dataframe_representation(norm_corpus):
    # get all unique words in the corpus
    cv = CountVectorizer(min_df=0., max_df=1.)
    cv_matrix = cv.fit_transform(norm_corpus)
    vocab = cv.get_feature_names()
    # show document feature vectors
    pd.DataFrame(cv_matrix, columns=vocab)

arguments = [
    Args(count_vectorizer('The sky is blue and beautiful.' 'Love this blue and beautiful sky!')),
    Args(count_vectorizer('The quick brown fox jumps over the lazy dog.')),
    Args(count_vectorizer("A king's breakfast has sausages, ham, bacon, eggs, toast and beans")),
    Args(count_vectorizer('I love green eggs, ham, sausages and bacon!')),
    Args(count_vectorizer('The brown fox is quick and the blue dog is lazy!')),
    Args(count_vectorizer('The sky is very blue and the sky is very beautiful today')),
    Args(count_vectorizer('The dog is lazy but the brown fox is quick!')),
]

exo_dataframe_representation = ExerciseFunction(
    dataframe_representation,
    arguments
)

# TF-IDF Model 

from sklearn.feature_extraction.text import TfidfVectorizer

def TfidfVectorizer(norm_corpus):
    tv = TfidfVectorizer(min_df=0.,
                        max_df=1.,
                        norm='l2',
                        use_idf=True,
                        smooth_idf=True)
    tv_matrix = tv.fit_transform(norm_corpus)
    tv_matrix = tv_matrix.toarray()

    vocab = tv.get_feature_names()
    return pd.DataFrame(np.round(tv_matrix, 2), columns=vocab)