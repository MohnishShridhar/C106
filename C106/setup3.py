import plotly.express as px
import csv
import numpy as np

def plotFigure(data_path):
    with open(data_path) as csv_file:
        df= csv.DictReader(csv_file)
        fig= px.scatter(df, x="Days Present", y="Marks In Percentage")
        fig.show()

def getDataSource(data_path):
    marks_in_percentage=[]
    days_present=[]
    with open(data_path) as csv_file:
        csv_reader= csv.DictReader(csv_file)
        for row in csv_reader:
            days_present.append(float(row["Days Present"]))
            marks_in_percentage.append(float(row["Marks In Percentage"]))
    
    return {"x":days_present, "y":marks_in_percentage}

def findCorrelation(dataSource):
    correlation=np.corrcoef(dataSource["x"], dataSource["y"])
    print("correlation between days present and marks in percentage: ", correlation[0,1])

def setup():
    data_path = "marksvsdays.csv"
    dataSource = getDataSource(data_path)
    findCorrelation(dataSource)
    plotFigure(data_path)

setup()