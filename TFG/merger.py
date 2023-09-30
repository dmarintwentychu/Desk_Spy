import pandas as pd



dfKeyLogs = pd.read_csv("./Dataset/keylog.csv") 
dfTestLogs = pd.read_csv("./Dataset/test.csv") 

dfFinal = pd.merge(dfTestLogs,dfKeyLogs, how ="outer", on=["Time","Time"])

dfFinal = dfFinal.drop(columns=["Unnamed: 0_x","Unnamed: 0_y"])



dfFinal.to_csv("./Dataset/dfFinalTest.csv")

