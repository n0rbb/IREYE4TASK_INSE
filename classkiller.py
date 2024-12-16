import pandas as pd
namae = ["data_joined13", "lstm_experiment1", "lstm_experiment2", "lstm_experiment_6s_1", "lstm_experiment_6s_2", "lstm_experiment_10s_1", "lstm_experiment_2s_1"] #No se simplifica para experiment0

def filter_rows_by_values(df, col, values):
        return df[~df[col].isin(values)]

for elem in namae:
    df = pd.read_csv(elem + ".csv", header = 0, sep = ",", dtype = {'Var1' : 'string', 'Var2' : 'string'})
    if elem == "data_joined13":
        colname = 'Var2'
        colname2 = 'Var1'
    else: 
        colname = '1' #Siempre en colname1 vamos a tener datos de clase para los datos de lstm. 
        
    if elem == "lstm_experiment1" or elem == "lstm_experiment_6s_1" or elem == "lstm_experiment_10s_1" or elem == "lstm_experiment_2s_1": #Estas dos están pensadas ya para el experimento 1. Debería simplificar esta línea
        df = filter_rows_by_values(df, colname, ["spkL","lisnL", "preTask"])
    elif elem == "lstm_experiment2" or elem == "lstm_experiment_6s_2" : #Estas dos, para el 2
         df = filter_rows_by_values(df, colname, ["comL", "cogL", "perL", "phyL", "aftExp", "befExp"])
    else: #data_joined has both experiment columns
        #Destruir clases para el experimento 1
        df = filter_rows_by_values(df, colname, ["spkL","lisnL", "preTask"])
        #Destruir clases para el experimento 2
        df = filter_rows_by_values(df, colname2, ["comL", "cogL", "perL", "phyL", "aftExp", "befExp"])

    print(df)
    df.to_csv(elem + "_touched.csv", sep = ",", index = False)