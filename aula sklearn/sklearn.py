from sklearn.tree import DecisionTreeClassifier
x= [
        [1, 0, 1, 0],  # febre, tosse, congestão nasal, dor de garganta
        [0, 1, 0, 1],  # sem febre, tosse, sem congestão nasal, dor de garganta
        [1, 1, 1, 0],  # febre, tosse, congestão nasal, sem dor de garganta
        [0, 1, 1, 1],  # sem febre, tosse, congestão nasal, dor de garganta
        [0, 0, 1, 1]  # sem febre, sem tosse, congestão nasal, dor de garganta
    ]
y = ["Gripe", "Resfriado Comum", "Sinusite","Gripe","Resfriado comum"]
clf = DecisionTreeClassifier()
clf.fit(x,y)

print("Você tem febre?")
febre = input()
if febre == "sim":
    febre = 1
elif febre == "não":
    febre = 0
else:
    print("Resposta inválida")

print("Você tem tosse?")

tosse = input()
if tosse == "sim":
    tosse = 1
elif tosse == "não":
    tosse = 0
else:
    print("Resposta inválida")

print("Você tem congestão nasal?")

congestão_nasal = input()
if congestão_nasal == "sim":
    congestão_nasal = 1
elif tosse == "não":
    congestão_nasal = 0
else:
    print("resposta inválida")

print("Você tem dor de garganta?")

dor = input()
if dor == "sim":
    dor = 1
elif dor == "não":
    dor = 0
else:
    print("resposta inválida")
    
print(clf.predict([0,0,0,0]))
    