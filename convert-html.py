from classes.Convert import Convert
import argparse

parser = argparse.ArgumentParser(description="Example script")
parser.add_argument('file', help='The file to convert')
args = parser.parse_args()

print("Converting")
convert = Convert('example-data/' + args.file + '.html', 'example-data/' + args.file + '.csv')
convert.convert()
print("Finished converting")