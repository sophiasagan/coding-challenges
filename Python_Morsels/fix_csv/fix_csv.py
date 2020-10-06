# from argparse import ArgumentParser
# import csv


# parser = ArgumentParser()
# parser.add_argument('old_filename')
# parser.add_argument('new_filename')
# args = parser.parse_args()

# with open(args.old_filename, newline='') as old_file:
#     rows = list(csv.reader(old_file, delimiter='|'))

# with open(args.new_filename, mode='wt', newline='') as new_file:
#     csv.writer(new_file).writerows(rows)

# Bonus 1

# from argparse import ArgumentParser
# import csv


# parser = ArgumentParser()
# parser.add_argument('old_filename')
# parser.add_argument('new_filename')
# parser.add_argument('--in-delimiter', dest='delim')
# parser.add_argument('--in-quote', dest='quote')
# args = parser.parse_args()

# with open(args.old_filename, newline='') as old_file:
#     quotechar = '"'
#     delimiter = '|'
#     if args.delim:
#         delimiter = args.delim
#     if args.quote:
#         quotechar = args.quote
#     reader = csv.reader(old_file, delimiter=delimiter, quotechar=quotechar)
#     rows = list(reader)

# with open(args.new_filename, mode='wt', newline='') as new_file:
#     writer = csv.writer(new_file)
#     writer.writerows(rows)

# Bonus 2

from argparse import ArgumentParser
import csv


parser = ArgumentParser()
parser.add_argument('old_filename')
parser.add_argument('new_filename')
parser.add_argument('--in-delimiter', dest='delim')
parser.add_argument('--in-quote', dest='quote')
args = parser.parse_args()

with open(args.old_filename, newline='') as old_file:
    arguments = {}
    if args.delim:
        arguments['delimiter'] = args.delim
    if args.quote:
        arguments['quotechar'] = args.quote
    if not args.delim and not args.quote:
        arguments['dialect'] = csv.Sniffer().sniff(old_file.read())
        old_file.seek(0)
    reader = csv.reader(old_file, **arguments)
    rows = list(reader)

with open(args.new_filename, mode='wt', newline='') as new_file:
    writer = csv.writer(new_file)
    writer.writerows(rows)