
from dfProcess import anime_df






results={}



def filterGetAnimeName(df, colValue):
  name_row_list = []
  if (colValue.islower() == True):
    name_df = df[df["Name lowercase"].str.contains(colValue)]
    for index, rows in name_df.iterrows():
       my_list =[rows['Name lowercase'], rows['English name lowercase']]
       name_row_list.append(my_list)
  else:
    name_df = df[df["Name"].str.contains(colValue)]
    for index, rows in name_df.iterrows():
       my_list =[rows['Name'], rows['English name']]
       name_row_list.append(my_list)

  return name_row_list


def filterGetAnimGenre(df, colName, colValue):
  genre_df = df[df[colName].str.contains(colValue)]
  genre_row_list = []
  for index, rows in genre_df.iterrows():
      # Create list for the current row
      my_list =[rows.Genres]
      # append the list to the final list
      genre_row_list.append(my_list)

  return genre_row_list

def filterGetAnimRatings(df, colName, colValue):
  ratings_df = df[df[colName].str.contains(colValue)]
  ratings_row_list = []
  for index, rows in ratings_df.iterrows():
      # Create list for the current row
      my_list =[rows.Score]
      # append the list to the final list
      ratings_row_list.append(my_list)

  return ratings_row_list


def filterGetAnimGenreSet(df, colName, colValue1, colValue2, colValue3):
  genre_df = df[df[colName].str.contains(colValue1) & df[colName].str.contains(colValue2) & df[colName].str.contains(colValue3)]
  genre_row_list = []
  genre_rating_List=[]
  for index, rows in genre_df.iterrows():
      # Create list for the current row
      my_list =rows.Name
      ratings= rows.Score
      # Create list for the current row
      # append the list to the final list
      genre_row_list.append(my_list)
      genre_rating_List.append(ratings)
      if rows.Score!= "Unknown":
          # result_andRatings.loc[len(result_andRatings)] = [rows.Name, float(rows.Score)]
          # result_andRatings.drop_duplicates(keep="first")
          results[rows.Name]= float(rows.Score)
      else:
        results[rows.Name]= float(0)



# functions to use for filtering with query search 
def filterWithQuery(df, getQuery):
  query_list =[]
  for token in getQuery:
    result = filterGetAnimeName(df, token)
  for name in result:
    query_list.append(name)
  return query_list


def genresSelected(query):
  query = query[0].split(',')
  for genre1 in range(len(query)):
    for genre2 in range(genre1, len(query)):
      for genre3 in range(genre2, len(query)):
        if genre1 != genre2 & genre2 != genre3:
          filterGetAnimGenreSet(anime_df, 'Genres', query[genre1], query[genre2], query[genre3])

# filter based on ratings, create 3 dataframes based on high, mid, low rating, sort within dataframe
def sortByRatings():
  rank= sorted(results.items(), key=lambda x:x[1],reverse=True)
  return rank

resultNum= len(results)