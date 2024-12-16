import pandas as pd
namae = ["data_joined13", "lstm_experiment1", "lstm_experiment2"] #No se simplifica para experiment0

def filter_rows_by_values(df, col, values):
        return df[~df[col].isin(values)]

for elem in namae:
    df = pd.read_csv(elem + ".csv", header = 0, sep = ",", dtype = {'Var1' : 'string', 'Var2' : 'string'})
    if elem == "data_joined13":
        colname = 'Var2'
        colname2 = 'Var1'
    else: 
        colname = '1'
        
    #Kill classes for experiment 1
    df = filter_rows_by_values(df, colname, ["spkL","lisnL", "preTask"])
    
    if elem == "data_joined13":
        #Kill classes for experiment 2
        df = filter_rows_by_values(df, colname2, ["comL", "cogL", "perL", "phyL", "aftExp", "befExp"])

    print(df)
    df.to_csv(elem + "_touched.csv", sep = ",", index = False)