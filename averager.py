import pandas as pd


ojitos = [0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]

cols = ["task", "perform", "eyestate"]
for i in range(28):
    cols.append("x" + str(i))
for i in range(28):
    cols.append("y" + str(i))
#class = ["Task", "lisnH", "lisnL", "pause", "preTask"] 
for i in range(20): 
    nes = "eye" + str(ojitos[i]) + "_sub" + str(i + 1)
    df = pd.read_csv(nes + ".csv", header = 0, sep = ",", dtype = {'Var1' : 'string', 'Var2' : 'string'})
    df.drop(columns = ['timestamp'], inplace = True)
   # print(df)
    dfavg = df.groupby(["Var1", "Var2"]).mean()
    print(dfavg)
    dfavg.reset_index(inplace = True)
    dfavg.to_csv(nes + "_mean.csv", sep = ",", index = False)
    
