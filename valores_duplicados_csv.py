import csv,collections,sys

try:
    file = sys.argv[1]
    argc= len(sys.argv)
    lista = list()
    if argc==2:
        csvfile = open(file,encoding="utf-8") 

        spamreader = csv.reader(csvfile,delimiter="," )
        
        for row in spamreader:
            lista.append(row[1])
        pass
    else:
        print("Uso: python3 valores_duplicados_csv nombredearchivo.csv")
        pass
    print("\n Valores duplicados: ")
    print([item for item, count in collections.Counter(lista).items() if count > 1])
except FileNotFoundError:
    print("El archivo no  ha sido encontrado.")
except IndexError:
    print("Uso: python3 valores_duplicados_csv nombredearchivo.csv")



