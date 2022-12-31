
from queryProcess import processInput
from queryProcess import tfidfAfterQuery
from filter import filterWithQuery
from filter import genresSelected
from filter import sortByRatings
from filter import filterGetAnimGenre
import filter
import dfProcess
from similarity import getTopResult




# full algorythm
def main(query):  
  ranking={}  
      # enter query, get tokens list
  getQuery, stringQuery= processInput(query)
  
 
  try:
     
    if stringQuery!= None or stringQuery != " ":
          # filter through anime datf
      queryList = filterWithQuery(dfProcess.useanime,getQuery)
      

      topResult= getTopResult(queryList, getQuery)
      filter.results={topResult[0]:12}
    genre= filterGetAnimGenre(dfProcess.useanime, 'Name lowercase',topResult[0])
    genresSelected(genre[0])  #Aisha main output put here as input
    ranking= sortByRatings()
    
    return list(ranking.keys())
    
    # else:
  except:
    error=["anime not available, please go back and try again"]
    return error



# test= main("Naruto")

# print(test)
