import pandas as pd
import numpy as np

ojitos = [0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]

def sul(lx, cx, rx, ly, cy, ry):
    slope1 = (cy - ly)/(cx - lx)
    slope2 = (cy - ry)/(cx - rx)
    return slope1 + slope2

def tul(lx, cx, rx, ly, cy, ry):
    scalarprod = (lx - cx)*(rx - cx) + (ly - cy)*(ry - cy)
    moduloa = np.sqrt((lx - cx)**2 + (ly - cy)**2)
    modulob = np.sqrt((rx - cx)**2 + (ry - cy)**2)
    #print(moduloa)
    return np.arccos(scalarprod/(moduloa * modulob))

def ir0(cornera, cornerb, x13, x14, x15, x17, x18, x19):
    center = np.max([x13, x14, x15]) - np.min([x17, x18, x19])
    return (center - cornera)/(cornerb - cornera)

def dtp(y20, y21, y27, y12, y13, y19, y15, y16, y17):
    return (np.max([y20, y21, y27]) - np.min([y12, y13, y19]))/(np.max([y15, y16, y17]) - np.min([y12, y13, y19]))

def dbp(y23, y24, y25, y12, y13, y19, y15, y16, y17):
     return (np.max([y15, y16, y17]) - np.min([y23, y24, y25]))/(np.max([y15, y16, y17]) - np.min([y12, y13, y19]))


#def tasking(taskvar):
#    taskvar.astype(dtype=str)
#    if taskvar == "pause":
#        return 0 #inactive
#    else:
#        return 1


for i in range(20):
    nes = "eye" + str(ojitos[i]) + "_sub" + str(i + 1) 
    df = pd.read_csv(nes + ".csv", header = 0, sep = ",", dtype = {'Var1' : 'string', 'Var2' : 'string'})
    #Parámetros sugeridos del párpado
    df['SUL1'] = sul(df['x2'], df['x3'], df['x4'], df['y2'], df['y3'], df['y4'])
    #print(df['x2'])
    df['TUL1'] = tul(df['x2'], df['x3'], df['x4'], df['y2'], df['y3'], df['y4'])
    df['SUL2'] = sul(df['x1'], df['x3'], df['x5'], df['y1'], df['y3'], df['y5'])
    df['TUL2'] = tul(df['x1'], df['x3'], df['x5'], df['y1'], df['y3'], df['y5'])
    df['SUL3'] = sul(df['x0'], df['x3'], df['x6'], df['y0'], df['y3'], df['y6'])
    df['TUL3'] = tul(df['x0'], df['x3'], df['x6'], df['y0'], df['y3'], df['y6'])

    df['SLL1'] = sul(df['x10'], df['x9'], df['x8'], df['y10'], df['y9'], df['y8'])
    df['TLL1'] = tul(df['x10'], df['x9'], df['x8'], df['y10'], df['y9'], df['y8'])
    df['SLL2'] = sul(df['x11'], df['x9'], df['x7'], df['y11'], df['y9'], df['y7'])
    df['TLL2'] = tul(df['x11'], df['x9'], df['x7'], df['y11'], df['y9'], df['y7'])
    df['SLL3'] = sul(df['x0'], df['x9'], df['x6'], df['y0'], df['y9'], df['y6'])
    df['TLL3'] = tul(df['x0'], df['x9'], df['x6'], df['y0'], df['y9'], df['y6'])

    #Parámetros sugeridos del iris - posición y oclusión
    df['IR0'] = ir0(df['x0'], df['x7'], df['x13'], df['x14'], df['x15'], df['x17'], df['x18'], df['x19']) #Posición del centro del iris
    df['IR1'] = tul(df['x19'], df['x12'], df['x13'], df['y19'], df['y12'], df['y13']) #Ángulos de oclusión top
    df['IR2'] = tul(df['x18'], df['x16'], df['x17'], df['y18'], df['y16'], df['y17']) #bottom

    #Parámetros sugeridos de a pupila - distancias a los bordes del iris (indicador de tamaño)
    df['PU0'] = dtp(df['y20'], df['y21'], df['y27'], df['y12'], df['y13'], df['y19'], df['y15'], df['y16'], df['y17'])
    df['PU1'] = dbp(df['y23'], df['y24'], df['y25'], df['y12'], df['y13'], df['y19'], df['y15'], df['y16'], df['y17'])
    df['PU2'] = df['PU0'] - df['PU1']
    df['ACTIVE'] = (df['Var2'] != "pause").astype(int)
    df.reset_index(inplace = True)
    #print(df)   
    df.to_csv(nes + "_extracted.csv", index = False)