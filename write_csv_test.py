import os
from write_csv_lib import *

my_dir = os.path.dirname(os.path.realpath(__file__))
csv_ofname = '00_output_good.csv'
full_ofname = my_dir + '/' + csv_ofname

key_list = ['a', 'b', 'c', 'd', 'e', 'f']
value_list = ['Anita', 'Brahma', 'Casa Verde', 'Dominik',
    'Elephant', 'Froedrick Frankenstein']

write_data_to_file(full_ofname, key_list, value_list)

# Now read it and spew

with open(full_ofname, 'r') as infile:
    for row in infile:
        print(row, end='')
