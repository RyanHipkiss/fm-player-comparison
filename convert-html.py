from classes.Convert import Convert

print("Converting")
convert = Convert('example-data/search.html', 'example-data/search.csv')
convert.convert()
print("Finished converting")