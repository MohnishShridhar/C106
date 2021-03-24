import plotly.express as px
import csv
import numpy as np

def plotFigure(data_path):
    with open(data_path) as csv_file:
        df= csv.DictReader(csv_file)
        fig= px.scatter(df, x="Coffee in ml", y="sleep in hours")
        fig.show()

def getDataSource(data_path):
    sleep_in_hours=[]
    coffee_in_ml=[]
    with open(data_path) as csv_file:
        csv_reader= csv.DictReader(csv_file)
        for row in csv_reader:
            coffee_in_ml.append(float(row["Coffee in ml"]))
            sleep_in_hours.append(float(row["sleep in hours"]))
    
    return {"x":coffee_in_ml, "y":sleep_in_hours}

def findCorrelation(dataSource):
    correlation=np.corrcoef(dataSource["x"], dataSource["y"])
    print("correlation between coffee in ml and sleep in hours: ", correlation[0,1])

def setup():
    data_path = "coffeevssleep.csv"
    dataSource = getDataSource(data_path)
    findCorrelation(dataSource)
    plotFigure(data_path)

setup()