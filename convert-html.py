from classes.Convert import Convert

print("Converting")
convert = Convert('example-data/wolves-moneyball-example-player-list.html', 'example-data/wolves-moneyball-example-player-list.csv')
convert.convert()
print("Finished converting")