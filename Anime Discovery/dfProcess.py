import pandas as pd
import os

current= os. getcwd()

mainDF=pd.read_csv("Anime Discovery/Data/anime.csv")
newanime= "Anime Discovery/Data/animeProcessed.csv"
# df list needed
useanime= pd.read_csv("Anime Discovery/Data/animeProcessed.csv")

def processAnime(df):
    # make this a pre process function
    # making a new dataframe where names are in lowercase
    # df = pd.read_csv(current+"/Data/anime.csv")

    # pd.set_option('display.max_rows', None)
    df.head()
    # copy the name columns into a new df
    copy_df = df[["Name","English name"]].copy()
    # make each column into lowercase
    copy_df['Name']= copy_df['Name'].str.lower()
    copy_df['English name'] = copy_df['English name'].str.lower()
    # rename column names
    copy_df.columns = ['Name lowercase', 'English name lowercase']
    copy_df

    # insert columns from the copy_df with lowercase to the original df in specific places
    df.insert(2, 'Name lowercase', copy_df['Name lowercase'])
    df.insert(6, 'English name lowercase', copy_df['English name lowercase'])
    # once you run this part, the original df will already have the columns inserted which is why its commented out
    return df

anime_df = processAnime(mainDF)

anime_df.to_csv(newanime, index= False, header=anime_df.columns.values)

