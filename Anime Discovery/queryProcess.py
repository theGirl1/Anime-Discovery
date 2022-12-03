from filter import filterGetAnimeName

import pandas as pd
import numpy as np
import nltk
import os
from typing import NamedTuple
from pandas.core.api import DataFrame
from sklearn.feature_extraction.text import TfidfVectorizer



# functions to use for filtering with query search 

def tfidfAfterQuery(querylist):
  # 
  place_string = []
  for name in querylist:
    place_string.append(' '.join(name))

  tfidf = TfidfVectorizer()
  tfs = tfidf.fit_transform(place_string)
  feature_names = tfidf.get_feature_names_out()
  dense = tfs.todense()
  denselist = dense.tolist()
  df = pd.DataFrame(denselist, columns=feature_names)
  
  return df

# clean up user input


def cleanQuery(keywords):
  stringQuery=""
  keywords= keywords.lower()
  stringQuery=keywords
  # remove punctuation
  from string import digits, punctuation
  keywords = keywords.translate(str.maketrans('', '',punctuation))
  return keywords, stringQuery

def processInput(query):

  keyword, stringQuery= cleanQuery(query)
  return keyword.split(), stringQuery

  




