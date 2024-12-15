from pandas import read_csv

ojitos = [0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]

#colacao = ["X, X, timestamp, X, eyestate"]

#for i in range(27):
#    colacao.append("x" + str(i))
#for i in range(27):
#    colacao.append("y" + str(i))

for i in range(19):
    nes = "eye" + str(ojitos[i]) + "_sub" + str(i + 1) 
#nes = "eye0_sub20"
df = read_csv(nes + ".txt", header = None, sep = " ")
df.to_excel(nes + ".xlsx", index = False, header = None)