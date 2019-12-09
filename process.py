import difflib
import re
import os

path = b'C:\Users\katya\PycharmProjects\untitled7'
folder = b'C:\Users\katya\PycharmProjects\untitled7\\titles'

list_with_sets = [(set(filter(None, re.split(r'\W| ', ' '.join(
    [open('titles/' + os.listdir('titles/')[i] + '/' + file, 'r').read().lower()
     + "\n" for file in
     [os.listdir('titles/' + topic) for topic in os.listdir('titles')][
         i]])))))
               for i in range(len(os.listdir('titles/')))]


output = [dI for dI in os.listdir(folder) if os.path.isdir(os.path.join(folder,dI))]
dict_with_themes = dict(zip(output, list_with_sets))

# f = open('C:\\Users\katya\PycharmProjects\\untitled7\\124146', 'r')
# print(type(f.read()))
# concrete_file = set(filter(None, re.split(r'\W| ', ' '.join(f.read().lower()))))
# print(concrete_file)
ls = set(filter(None, __import__('re').split(r'\W| ', open('51122', 'r').read().lower())))
# with open('C:\\Users\katya\PycharmProjects\\untitled7\\124146') as f:
#     ls = set([word for line in f for word in line.split()])
# print(ls)
# for key, value in a_dict.items():
# ...     print(key, '->', value)
# f = open('text.txt', 'r')
# >>> l = [line.strip() for line in f]
for key, value in dict_with_themes.items():
    res = len(value) - len(set(value) - set(ls))
    print(res, key)
