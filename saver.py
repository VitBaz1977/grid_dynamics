import csv

def save_to_csv(fname,Data1):
    myFile = open(fname, 'w')
    with myFile:
        writer = csv.writer(myFile)
        writer.writerows(Data1)
    print("Writing complete")
