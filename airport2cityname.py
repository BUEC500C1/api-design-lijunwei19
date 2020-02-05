import csv

def Airport2CN(Name_of_airprot):

  dic={ }

  filename = "airports.csv"

  with open(filename, 'r') as csvfile:

    csvreader = csv.reader(csvfile)

    for row in csvreader:

      # print(row)

      dic[ row[3].lower() ] = ( row[8].lower(), row[10].lower())

  return dic[ Name_of_airprot.lower()]
   

# def main():

#   print(Airport2CN("Total Rf Heliport".lower()))
#   print(Airport2CN("Kitchen Creek Helibase Heliport".lower()))
#   print(Airport2CN("Lt World Airport".lower()))
#   print(Airport2CN("Bailey Generation Station Heliport".lower()))

# if __name__ == '__main__':

#   main()


