### Code does not run
import requests
from bs4 import BeautifulSoup
import pandas as pd

elections=[]
for year in range(1924, 2013, 4):
    year=str(year)
    file_name= year + ".csv"
    header=pd.read_csv(file_name, nrows=1).dropna(axis=1)
    d=header.iloc[0].to_dict()

    votes=pd.read_csv(file_name, index_col=0, thousands= ",", skiprows=[1])
    votes.rename(inplace=True, columns=d)
    votes.dropna(inplace=True, axis=1)

    votes["Year"]=year
    ### What is df? It isn't defined
    elections.append(df[["Democratic", "Republican", "Total Votes Cast", "Year"]])

    results=pd.concat(elections)
    results["Republican Vote Share"]=results["Republican"]/results["Total Votes Cast"]

graph=results[results.index=="Accomack County"].plot(x="Year", y="Republican Vote Share")
graph.get_figure().savefig('accomack.png')
