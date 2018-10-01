# 3.7 자료구조를 더 크게

marxes = ['Groucho', 'Chico', 'Harpo']
pythons = ['Chapman', 'Cleese', 'Gilliam', 'Jones', 'Palin']
stooges = ['Moe', 'Curly', 'Larry']


tuple_of_lists = marxes, pythons, stooges
tuple_of_lists
# (['Groucho', 'Chico', 'Harpo'], ['Chapman', 'Cleese', 'Gilliam', 'Jones', 'Palin'], ['Moe', 'Curly', 'Larry'])


list_of_lists = [marxes, pythons, stooges]
list_of_lists
# [['Groucho', 'Chico', 'Harpo'], ['Chapman', 'Cleese', 'Gilliam', 'Jones', 'Palin'], ['Moe', 'Curly', 'Larry']]


dict_of_lists = {'Marxes': marxes, 'Pythons': pythons, 'Stooges': stooges}
dict_of_lists
# {'Marxes': ['Groucho', 'Chico', 'Harpo'], 'Pythons': ['Chapman', 'Cleese', 'Gilliam', 'Jones', 'Palin'], 'Stooges': ['Moe', 'Curly', 'Larry']}


houses = {
    (44.79, -93.14, 285): 'My House',
    (38.89, -77.03, 13): 'The White House'
    }
