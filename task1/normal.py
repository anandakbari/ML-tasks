modern_family = ['CLaiRe_DunPhY', 'PHiL_dUnpHY', 'GLoRiA_PriTCheTt', 'CaMErOn_TuCKEr',
'StELLa']

indices,characters=[],[]


for index in enumerate(modern_family):
    indices.append(index[0])
    characters.append(index[1].lower().replace("_","-"))


length=lambda string:len(string)

temp=list(map(length,characters))

indices=list(map(sum,zip(indices,temp)))
indices.sort(reverse=True)


phew_finally = {}
for key in indices:
    for value in characters:
        phew_finally[key] = value
        characters.remove(value)
        break

print(phew_finally)



