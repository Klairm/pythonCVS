import csv,collections,sys

def csv_check():
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
            print("Usage: python3 duplicated-csv-values.py <file.csv>")
            pass
        print("\n Duplicated values: ")
        print([item for item, count in collections.Counter(lista).items() if count > 1])
        
    except FileNotFoundError:
        print("File not found.")
    except IndexError:
        print("Usage: python3 duplicated-csv-values.py <file.csv>")


csv_check()




