import string
import random
in_string = "dfsf jjk jk k SDFF sd sdffdfs sdf SDF"
print(string.punctuation)
for char in string.punctuation:
    in_string = in_string.replace(char, ' ')
in_string = in_string.lower().split()
print("Количество слов:", len(in_string))