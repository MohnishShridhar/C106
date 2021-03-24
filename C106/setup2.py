import plotly.express as px
import csv
import numpy as np

def plotFigure(data_path):
    with open(data_path) as csv_file:
        df= csv.DictReader(csv_file)
        fig= px.scatter(df, x="TV size", y="Time")
        fig.show()

def getDataSource(data_path):
    time=[]
    tv_size=[]
    with open(data_path) as csv_file:
        csv_reader= csv.DictReader(csv_file)
        for row in csv_reader:
            tv_size.append(float(row["TV size"]))
            time.append(float(row["Time"]))
    
    return {"x":tv_size, "y":time}

def findCorrelation(dataSource):
    correlation=np.corrcoef(dataSource["x"], dataSource["y"])
    print("correlation between tv size and time spent watching: ", correlation[0,1])

def setup():
    data_path = "sizevstime.csv"
    dataSource = getDataSource(data_path)
    findCorrelation(dataSource)
    plotFigure(data_path)

setup()