import regex as re
import pandas as pd
import spacy
import numpy as np
from matplotlib import pyplot as plt
import sklearn
from sklearn.datasets import load_files
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import MiniBatchKMeans
import os
import nltk
from configs import DATA_PATH, FGD_FILE_NAME, SIF_FILE
from nltk.corpus import brown
from nlp import sample_analyze_sentiment
from google.cloud import language_v1
from google.cloud.language_v1 import enums


# texts = open(SIF_FILE, "r")
text = open(r"C:\dev\data\josh-fyp\inputs\FGD_data\SIF\SIF3.txt", "r")
texts = text.readlines()

with open(r"C:\dev\data\josh-fyp\inputs\FGD_data\SIF\SIF3.txt", "r") as fd:
    text = fd.read()

SCH_partitions = []

# for line in texts:

schools = re.split(r"School [nN]ame:", text)

# pip install spacy
# python -m spacy download en




clean_schools = re.sub(r"\p{P}+", "", schools_str)
# remove stop words before vocab

vocab = sorted(set(
    clean_schools.split()
))
tokens_without_sw = [word for word in vocab if not word in all_stopwords]
clean_schools_2 = re.sub(r"\s([P]|[p])\s", " ", clean_schools)

# stemming



print(len(vocab), vocab)

def binary_transform(text):
    # create a vector with all entries as 0
    output = np.zeros(len(vocab))
    # tokenize the input
    words = set(text.split())
    # for every word in vocab check if the doc contains it
    for i, v in enumerate(vocab):
        output[i] = v in words
    return output

ans = print(binary_transform(schools_str))

# Appearances
# vec = CountVectorizer(binary=True)
# vec.fit(texts)
# print([w for w in sorted(vec.vocabulary_.keys())])

# ans = pd.DataFrame(vec.transform(texts).toarray(), columns=sorted(vec.vocabulary_.keys()))
#
# # Count
# vec = CountVectorizer(binary=False) # we could ignore binary=False argument since it is default
# vec.fit(texts)
# ans2 = pd.DataFrame(vec.transform(texts).toarray(), columns=sorted(vec.vocabulary_.keys()))
#
# print(ans)
# print(ans2)

# TF-IDF
vec = TfidfVectorizer()
vec.fit(schools)

ans3 = pd.DataFrame(vec.transform(schools).toarray(), columns=sorted(vec.vocabulary_.keys()))
print(ans3)
print(max(ans3))
