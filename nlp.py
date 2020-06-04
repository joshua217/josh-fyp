from google.cloud import language_v1
from google.cloud.language_v1 import enums

import argparse
import io
import json
import os

from google.cloud import language
import numpy
import six

text = open(r"C:\dev\data\josh-fyp\inputs\FGD_data\SIF\SIF3.txt", "r")
texts = text.readlines()

# FGD Analysis
with open(r"C:\dev\data\josh-fyp\inputs\FGD_data\SIF\SIF3.txt", "r") as fd:
    text = fd.read()
# sample_analyze_sentiment(text)

print("2 to 3", stats.mannwhitneyu(kk_wsh_merged_2[kk_wsh_merged_2['Q1'] == 2]['SmansoniPrev'],
                                   kk_wsh_merged_2[kk_wsh_merged_2['Q1'] == 3]['SmansoniPrev']))

print("1 to 2", stats.mannwhitneyu(kk_wsh_merged_2[kk_wsh_merged_2['Q1'] == 1]['SmansoniPrev'],
                                   kk_wsh_merged_2[kk_wsh_merged_2['Q1'] == 2]['SmansoniPrev']))

print("1 to 3", stats.mannwhitneyu(kk_wsh_merged_2[kk_wsh_merged_2['Q1'] == 1]['SmansoniPrev'],
                                   kk_wsh_merged_2[kk_wsh_merged_2['Q1'] == 3]['SmansoniPrev']))


os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'FGP_NLP_josh-fyp-294bc4b423e6.json'

def sample_analyze_sentiment(text_content):
    """
    Analyzing Sentiment in a String

    Args:
      text_content The text content to analyze
    """
    client = language_v1.LanguageServiceClient()

    type_ = enums.Document.Type.PLAIN_TEXT


    language = "en"
    document = {"content": text_content, "type": type_, "language": language}

    # Available values: NONE, UTF8, UTF16, UTF32
    encoding_type = enums.EncodingType.UTF8

    response = client.analyze_sentiment(document, encoding_type=encoding_type)
    # Get overall sentiment of the input document
    print(u"Document sentiment score: {}".format(response.document_sentiment.score))
    print(
        u"Document sentiment magnitude: {}".format(
            response.document_sentiment.magnitude
        )
    )

    # Get sentiment for all sentences in the document
    for sentence in response.sentences:
        print(u"Sentence text: {}".format(sentence.text.content))
        print(u"Sentence sentiment score: {}".format(sentence.sentiment.score))
        print(u"Sentence sentiment magnitude: {}".format(sentence.sentiment.magnitude))

    print(u"Language of the text: {}".format(response.language))


def classify(text, verbose=True):
    """Classify the input text into categories. """

    language_client = language.LanguageServiceClient()

    document = language.types.Document(
        content=text,
        type=language.enums.Document.Type.PLAIN_TEXT)
    response = language_client.classify_text(document)
    categories = response.categories

    result = {}

    for category in categories:
        # Turn the categories into a dictionary of the form:
        # {category.name: category.confidence}, so that they can
        # be treated as a sparse vector.
        result[category.name] = category.confidence

    if verbose:
        print(text)
        for category in categories:
            print(u'=' * 20)
            print(u'{:<16}: {}'.format('category', category.name))
            print(u'{:<16}: {}'.format('confidence', category.confidence))

    return result
