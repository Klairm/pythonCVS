import csv,collections,sys

try:
    file = sys.argv[1]
    lista = []
    if (len(sys.argv))==2: 
        csvfile = open(file,encoding="utf-8")  
        

        spamreader = csv.reader(csvfile,delimiter="," ) 
        for x,c in spamreader:
            lista.append(x)
            lista.append(c)
                
    else: 
        print("Uso: python3 valores_duplicados_csv nombredearchivo.csv") 
       
        
    print("\n Valores duplicados: ")
    print([item for item, count in collections.Counter(lista).items() if count > 1]) 
     
    
except FileNotFoundError:
    print("El archivo no  ha sido encontrado.")
except IndexError:
    print("Uso: python3 valores_duplicados_csv nombredearchivo.csv")



