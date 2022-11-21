import numpy as np

def cosine_similarity(x, y):
    
    # Ensure length of x and y are the same
    if len(x) != len(y) :
        return None
    
    # Compute the dot product between x and y
    dot_product = np.dot(x, y)
    
    # Compute the L2 norms (magnitudes) of x and y
    magnitude_x = np.sqrt(np.sum(x**2)) 
    magnitude_y = np.sqrt(np.sum(y**2))
    
    # Compute the cosine similarity
    cosine_similarity = dot_product / (magnitude_x * magnitude_y)
    
    return cosine_similarity

from sklearn.feature_extraction.text import CountVectorizer
def cosine(test_result):
    cos_test = []
    for name in test_result:
        cos_test.append(' '.join(name))
        # Create a matrix to represent the corpus
        matrix = CountVectorizer().fit_transform(cos_test).toarray()
        print(matrix)
        similarity = []
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                similarity.append(cosine_similarity(matrix[i], matrix[j]))
        



def getTopResult(resultList, getQuery):
  from sklearn.feature_extraction.text import CountVectorizer
  cos_test = []
  cos_test.append(' '.join(getQuery))
  for name in resultList:
    cos_test.append(' '.join(name))
  # Create a matrix to represent the corpus
  matrix = CountVectorizer().fit_transform(cos_test).toarray()
  similarity = []
  for i in range(len(matrix)):
    similarity.append(cosine_similarity(matrix[0], matrix[i]))
   
  max = 0
  pointer = 0
  for index in range(len(similarity)):
    if index != 0 and similarity[index] > max:
      max = similarity[index]
      pointer = index
  return resultList[pointer-1]