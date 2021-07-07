import string

str1 = string.ascii_lowercase

dictionary1 = {char:char for char in str1}
dictionary2 = {char:(char+char if i%2 ==0 else char) for i,char in enumerate(str1)}

dictionary3 = {'a': 'a', 'e': 'e', 'i': 'i', 'm': 'mm', 'q': 'qq', 'u': 'uu', 'y': 'yy'}

def left_join(dictionary1, dictionary2):
 k2dict = {key:(True if key in dictionary2.keys() else False) for key in dictionary2.keys()}
 return [[key, dictionary1[key], dictionary2[key]] if k2dict[key] else [key, dictionary1[key], None] for key in dictionary1]
