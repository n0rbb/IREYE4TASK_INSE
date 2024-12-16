import pandas as pd
import numpy as np

v = 0 #VARIABLE PARA ESCOGER EL EXPERIMENTO. SOLO DE 0 A 2 Y MEJOR NO HACER EL 0 
touched = 0
class0 = [0, 1]
if touched == 0:
    class1 = ['Task', 'lisnH', 'lisnL', 'pause', 'preTask', 'rating', 'spkH', 'spkL']
    class2 = ['aftExp', 'befExp', 'cogH', 'cogL', 'comH', 'comL', 'pause', 'perH', 'perL', 'phyH', 'phyL']
else:
    class1 = ['Task', 'lisnH', 'pause', 'preTask', 'rating', 'spkH']
    class2 = ['cogH', 'comH', 'pause', 'perH', 'phyH']
classeslist =  [class1, class2]
cnms = ['Var2', 'Var1']
classes = classeslist[v]
colname = cnms[v]

#La idea es obtener un nuevo dataset de unos 5s de cada clase, es decir, si la cámara va a 60Hz, unas 300 muestras


procdata = pd.DataFrame()
ojitos = [0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for i in range(20):
    if (ojitos[i] == 0) and i != 8:   #Me voy a quitar el sujeto 9 por los problemas de la grabación
        nes = "eye0_sub" + str(i + 1) + ".csv" #OJO, ME HE VENTILADO LAS CARACTERÍSTICAS
        df = pd.read_csv(nes, header = 0, sep = ",", dtype = {'Var1' : 'string', 'Var2' : 'string'})
        df = df.drop(columns=['timestamp', 'eyestate'])

        if v == 0:
            df = df.drop(columns=[cnms[1]])
        else:   
            df = df.drop(columns=[cnms[0]])
        #df_out = pd.DataFrame().reindex_like(df)
        print(df)
        #df_out2 = df.groupby('Var1').nth(list(range(300)))

        df_out = df.groupby(colname) 
        df_out1 = df_out.nth(list(range(240))) #DATOS DE LA MUESTRA 1 (4s)
        df_out2 = df_out.nth(list(range(240, 480))) #DATOS DE LA MUESTRA 2 (4s)
        #print(df_out1)
        #print(df_out2)

        for elem in classes:
            df_out1 = df_out1.reset_index(drop=True)
            df_out2 = df_out2.reset_index(drop=True)

           # print(df_out1)
           # print(df_out2)
    
            mask1 = df_out1[colname] == elem
            mask2 = df_out2[colname] == elem
            result = df_out1.loc[mask1]
            result = result.reset_index(drop=True)
            result2 = df_out2.loc[mask2]
            result2 = result2.reset_index(drop=True)
    
            #print(result)
            #print(result2)

            result = result.stack(dropna=False)
            result2 = result2.stack(dropna=False)

            result = pd.DataFrame([result.values])
            result2 = pd.DataFrame([result2.values])

            result['CLASS'] = elem
            result2['CLASS'] = elem

            procdata = pd.concat([procdata, result, result2], ignore_index = True)
            print(procdata)

procdata = procdata.fillna(0)


if touched == 0:
    ender = ".csv"
else:
    ender = "_touched.csv"

procdata.to_csv("lstm_experiment"+ str(v + 1) + "_reduced" + ender, index = False)



#print (df_out['Var2'].unique())
#df_out = df_out.stack()
#print(df_out)
#single_row = pd.DataFrame([df_out.values], columns=["param" + str(i) for i in range(5700)])
#df_out0 = df.groupby('ACTIVE').nth(list(range(300)))

#df_out2.to_csv("lstm_experiment2.csv", index = False)
#df_out.to_csv("lstm_experiment1.csv", index = False)
#df_out0.to_csv("lstm_experiment0.csv", index = False)



#print(single_row)