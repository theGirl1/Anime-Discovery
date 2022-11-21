
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
def main():  
  ranking={}  
      # enter query, get tokens list
  getQuery, stringQuery= processInput()
  
    
      
  try:
    
    
    if stringQuery!= None or stringQuery != " ":
          # filter through anime datf
      queryList = filterWithQuery(dfProcess.anime_df,getQuery)
      

      topResult= getTopResult(queryList, getQuery)
      filter.results={topResult[0]:12}
    genre= filterGetAnimGenre(dfProcess.anime_df, 'Name lowercase',topResult[0])
    print(genre)
    genresSelected(genre[0])  #Aisha main output put here as input
    ranking= sortByRatings()
    return ranking
    
    # else:
  except:
    print("anime not available, please go back and try again")
    ranking= main()
    return ranking

  

       

 
    
run=main()

print(run)


