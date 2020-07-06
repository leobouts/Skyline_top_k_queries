import csv


def generate_next_r1(number_of_valid_lines):

    with open('females_sorted') as r1:
        reader = csv.reader(r1, delimiter='\t')

        # try until we get valid tuple, in our case
        # above 18 and not married

        for tup in reader:

            tup_splitted = tup[0].split(',')

            if int(tup_splitted[1]) < 18 or tup_splitted[8].startswith(' Married'):
                continue

            else:
                number_of_valid_lines.append('1')
                yield tup_splitted


def generate_next_r2(number_of_valid_lines):

    with open('males_sorted') as r2:
        reader = csv.reader(r2, delimiter='\t')

        for tup in reader:

            tup_splitted = tup[0].split(',')

            if int(tup_splitted[1]) < 18 or tup_splitted[8].startswith(' Married'):
                continue

            else:
                number_of_valid_lines.append('1')
                yield tup_splitted
