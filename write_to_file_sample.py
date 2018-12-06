import os

def write_to_a_file(filename, stuff_to_write):
    """
    Sample code to show how to write to a file
    """
    print('starting write to a file')
    word = 'hello'
    name = 'frodo'
    with open(filename, 'w') as outf:
        outf.write('This is the firstline.\n')
        outf.write(stuff_to_write)
        outf.write('\n')
        outf.write(word + ',' + name)

    print('done')


if __name__ == '__main__':
    my_dir = os.path.dirname(os.path.realpath(__file__))

    # init the data to use
    text = 'This is the stuff to write.  Also this.'
    filename = 'sample_output.txt'
    ofname_full = my_dir + '/' + filename

    # call our function
    write_to_a_file(ofname_full, text)

    print('\n### now let\'s read the file and spew it\n')

    with open(ofname_full,'r') as inf:
        for row in inf:
            print(row, end='')

    print('all done')
