import pandas as pd
dfs = []
ojitos = [0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
for i in range(14, 20): #0-13 para los usuarios de entrenamiento. 14-20 para test. Descartamos ojo izquierdo para facilitar el aprendizaje. 
    if (ojitos[i] == 0): #Fuck left eye, eso es de rojos.
        nes = "eye" + str(ojitos[i]) + "_sub" + str(i + 1) + "_extracted"
        dfs.append(pd.read_csv(nes + ".csv", header = 0, sep = ",", dtype = {'Var1' : 'string', 'Var2' : 'string'}))

joined = pd.concat(dfs, ignore_index = True)
joined.to_csv("test_joined14-20.csv", sep = ",", index = False)