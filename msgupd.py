import dashx
def getvx(dict): 
    list = [] 
    for key in dict.values(): 
        list.append(key)
    return list
def getList(dict): 
    list = [] 
    for key in dict.keys(): 
        list.append(key)
    return list
E = dict(dashx.des1)
frontzwe = open('update.txt', 'r')
frontxwe = frontzwe.read()
P = eval(frontxwe)
x1 = set(P)-set(E)
x2 = set(E)-set(P)
x3 = list(x1)
x4 = list(x2)
if len(x2) != 0:
    u1 = list(x2)
    u2 = '\n'.join([u1[i] + ' - ' + E[u1[i]][1] for i in range(len(u1))])
    x2 = 'New Folder Added : ' + repr(x2) + '\n' + u2
    
if len(x1) != 0:
    x1 = "Folder Removed : "  + repr(x1)
    
if len(x1) == 0:
    x1 = "No Folder Removed"
    
if len(x2) == 0:
    x2 = "No Folder Added"

z1 = getList(P)
z2 = getList(E)

list_1 = eval(P[z1[0]][1])
list_2 = eval(E[z1[0]][1])
z5 = set(list_2)-set(list_1)
z8 = ''
if len(set(P)-set(E)) == 0:
    zs = ','.join(["'/" + z1[i] + "': " + '"' + str(list(set(eval(E[z1[i]][1]))-set(eval(P[z1[i]][1])))) + '"' for i in range(len(z1))])
    z6 = eval('{' + zs + '}')
    z7 = getList(z6)
    z8 = '\n'.join([z7[i] + " - " + ', '.join(map(str, eval(z6[z7[i]]))) for i in range(len(z1))  if len(eval(z6[z7[i]])) != 0])
if len(set(P)-set(E)) != 0:
    zs = ','.join(["'/" + z2[i] + "': " + '"' + str(list(set(eval(E[z2[i]][1]))-set(eval(P[z2[i]][1])))) + '"' for i in range(len(z2))])
    z6 = eval('{' + zs + '}')
    z7 = getList(z6)
    z8 = '\n'.join([z7[i] + " : " + ', '.join(map(str, eval(z6[z7[i]]))) for i in range(len(z2))  if len(eval(z6[z7[i]])) != 0])

msgupd = ''       
if len(set(P)-set(E)) == 0 and len(set(E)-set(P)) == 0 and z8 == '':
  msgupd = "No New Update"

if len(set(P)-set(E)) != 0 and len(set(E)-set(P)) != 0 and z8 != '':
  msgupd = f"◾Batches Updates - \n{z8}\n\n➕{x2}\n\n➖{x1}"

if len(set(P)-set(E)) != 0 and len(set(E)-set(P)) == 0 and z8 != '':
  msgupd = f"◾Batches Updates - \n{z8}\n\n➖{x1}"

if len(set(P)-set(E)) == 0 and len(set(E)-set(P)) != 0 and z8 != '':
  msgupd = f"◾Batches Updates - \n{z8}\n\n➕{x2}"

if len(set(P)-set(E)) == 0 and len(set(E)-set(P)) == 0 and z8 != '':
  msgupd = f"◾Batches Updates - \n{z8}"

if len(set(P)-set(E)) == 0 and len(set(E)-set(P)) != 0 and z8 == '':
  msgupd = f"➕{x2}"

if len(set(P)-set(E)) != 0 and len(set(E)-set(P)) == 0 and z8 == '':
  msgupd = f"➖{x1}"

if len(set(P)-set(E)) != 0 and len(set(E)-set(P)) != 0 and z8 == '':
  msgupd = f"➕{x2}\n\n➖{x1}"