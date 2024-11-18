# main file to read csv_file and import other files
import pandas as pd
import csv
import normalizedformtables
import data_parser
from outputallformtables import op1NF, op2_3_bcnf_4_5


# Reading the input csv file and the Functionaldependencies text file
input_file = pd.read_csv('exampleInputTable.csv')
print('GivenTable')
print(input_file)
print('\n')

with open('Functionaldependencies.txt', 'r') as file:
    lines = [line.strip() for line in file]

Functionaldependencies = {}
for line in lines:
    determinant, dependent = line.split(" -> ")
    # Splitting the determinant by comma to make it a list
    determinant = determinant.split(", ")
    Functionaldependencies[tuple(determinant)] = dependent.split(", ")
print('Functionaldependencies')
print(Functionaldependencies)
print('\n')

# Input from the user
HighestNormalform = input(
    'Choose Higehst Normal form table can reach (1: 1NF, 2: 2NF, 3: 3NF, B: BCNF, 4: 4NF, 5: 5NF): ')
if HighestNormalform in ["1", "2", "3", "4", "5"]:
    HighestNormalform = int(HighestNormalform)

# Find the highest normal form of the GivenTable
Give_highnf = int(
    input('Find the highest normal form of the input table? (1: Yes, 2: No): '))
high_nf = 'Not normalized yet to any normal form'

# Enter Key
Primarykey = input(
    "Enter Primary keys if it composite enter comma between them: ").split(', ')
print('\n')

keys = ()
for key in Primarykey:
    keys = keys + (key,)

Primarykey = keys

mvd_fds = {}
if not HighestNormalform == 'B' and HighestNormalform >= 4:
    with open('mvd_fds.txt', 'r') as file:
        mvd_lines = [line.strip() for line in file]

    print(mvd_lines)

    for mvd in mvd_lines:
        determinant, dependent = mvd.split(" ->> ")
        determinant = determinant.split(
            ", ") if ", " in determinant else [determinant]
        determinant_str = str(determinant)
        if determinant_str in mvd_fds:
            mvd_fds[determinant_str].append(dependent)
        else:
            mvd_fds[determinant_str] = [dependent]

    print('MULTI-VALUED Functionaldependencies')
    print(mvd_fds)
    print('\n')

input_file = data_parser.data_parser(input_file)

if HighestNormalform == 'B' or HighestNormalform >= 1:
    nfone_table, one_flag = normalizedformtables.normalizationform_one(
        input_file, Primarykey)

    if one_flag:
        high_nf = 'Highest Normal Form of input table is: 1NF'

    if HighestNormalform == 1:
        if one_flag:
            print('Already  1NF')
            print('\n')

        print('OUPUT QUERIES AFTER 1NF:')
        print('\n')
        op1NF(Primarykey, nfone_table)

if HighestNormalform == 'B' or HighestNormalform >= 2:
    nftwo_table, two_flag = normalizedformtables.normalizationform_two(
        nfone_table, Primarykey, Functionaldependencies)

    if one_flag and two_flag:
        high_nf = 'Highest Normal Form of input table is: 2NF'

    if HighestNormalform == 2:
        if two_flag and one_flag:
            print('Already  2NF')
            print('\n')

        print('OUPUT QUERIES AFTER 2NF:')
        print('\n')
        op2_3_bcnf_4_5(nftwo_table)

if HighestNormalform == 'B' or HighestNormalform >= 3:
    nfthree_table, three_flag = normalizedformtables.normalizationform_three(
        nftwo_table, Primarykey, Functionaldependencies)

    if one_flag and two_flag and three_flag:
        high_nf = 'Highest Normal Form of input table is: 3NF'

    if HighestNormalform == 3:
        if three_flag and two_flag and one_flag:
            print('Already  3NF')
            print('\n')

        print('OUPUT QUERIES AFTER 3NF:')
        print('\n')
        op2_3_bcnf_4_5(nfthree_table)

if HighestNormalform == 'B' or HighestNormalform >= 4:
    bcnfrel, bcnf_flag = normalizedformtables.bcnormalizationform(
        nfthree_table, Primarykey, Functionaldependencies)

    if one_flag and two_flag and three_flag and bcnf_flag:
        high_nf = 'Highest Normal Form of input table is: BCNF'

    if HighestNormalform == 'B':
        if bcnf_flag and three_flag and two_flag and one_flag:
            print('Already  BCNF')
            print('\n')

        print('OUPUT QUERIES AFTER BCNF:')
        print('\n')
        op2_3_bcnf_4_5(bcnfrel)

if not HighestNormalform == 'B' and HighestNormalform >= 4:
    nffour_table, four_flag = normalizedformtables.normalizationform_four(
        bcnfrel, mvd_fds)

    if one_flag and two_flag and three_flag and bcnf_flag and four_flag:
        high_nf = 'Highest Normal Form of input table is: 4NF'

    if HighestNormalform == 4:
        if four_flag and bcnf_flag and three_flag and two_flag and one_flag:
            print('Already Normalized to 4NF')
            print('\n')

        print('OUPUT QUERIES AFTER 4NF:')
        print('\n')
        op2_3_bcnf_4_5(nffour_table)

if not HighestNormalform == 'B' and HighestNormalform >= 5:
    nf5rel ,five_flag = normalizedformtables.normalizationform_five(
        nffour_table, Primarykey, Functionaldependencies)

    if one_flag and two_flag and three_flag and bcnf_flag and four_flag and five_flag:
        high_nf = 'Highest Normal Form of input table is: 5NF'

    if HighestNormalform == 5:
        if five_flag and four_flag and bcnf_flag and three_flag and two_flag and one_flag:
            print('Already Normalized to 5NF')
            print('\n')

        print('OUPUT QUERIES AFTER 5NF:')
        print('\n')
        op2_3_bcnf_4_5(nf5rel)

if Give_highnf == 1:
    print('\n')
    print(high_nf)
    print('\n')
