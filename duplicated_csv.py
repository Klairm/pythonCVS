import csv,collections
csvfile = open('filename.csv',encoding="utf-8") 
spamreader = csv.reader(csvfile,delimiter="," )
lista = list()
for row in spamreader:
	
	lista.append(row[1])
	print(lista[3:],end="" )

print("\n")
print("\n Duplicatess: ")
print([item for item, count in collections.Counter(lista).items() if count > 1])
