import csv,collections
csvfile = open('patch.csv',encoding="utf-8") 
spamreader = csv.reader(csvfile,delimiter="," )
lista = list()
for row in spamreader:
	
	lista.append(row[1])
	print(lista[3:],end="" )

print("\n")
print("\n Duplicados: ")
print([item for item, count in collections.Counter(lista).items() if count > 1])