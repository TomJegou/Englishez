lignes  = []
colonnes = []
d = []
v=[]
with open('Verbes irréguliers.txt','r') as verbes_txt:
    for ligne in verbes_txt.readlines():
        for lettre in ligne:
            if lettre == '\n':
                v.append(''.join(d))
                colonnes.append(v)
                v = []
                d = []

            elif lettre == '\t':
                v.append(''.join(d))
                colonnes.append(v)
                v = []
                d = []
            else:
                d.append(lettre)

        lignes.append(colonnes)
        colonnes = []



print(lignes)
print(lignes[134][0])
print(len(lignes))
del lignes[134]
print(lignes)
print(lignes[len(lignes)-1])
print(lignes[1][1][0])
print(len(lignes))