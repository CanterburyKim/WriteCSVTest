"""
Sample code to show how you can use enumerate to traverse two
lists simultaneously
"""
list_a = [0, 1, 2, 3, 4]
list_b = ['Able', 'Baker', 'Chumley', 'Doritos', 'Excelsior']

# Enumerate return first an incrementing counter as if you did
# for i in range( size_of_list_a ):
# and also returns each element in list a (that corresponds to that index)

for index, element_in_list_a in enumerate(list_a):
    print(f'the index is {index} and the list_a element is {element_in_list_a}')
    list_b_element = list_b[index]
    print(f'the list_b element is {list_b_element}')


# note : you can do this with any number of lists
