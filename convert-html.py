from classes.Convert import Convert

print("Converting")
convert = Convert('example-data/players.html', 'example-data/players.csv')
convert.convert()
print("Finished converting")