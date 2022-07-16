"""
import itertools

def FindAllCombination(val):
    string_combination = itertools.permutations(val)
    string_combination = list(string_combination)
    string_combination = [''.join(combination) for combination in string_combination]

    print(string_combination)


if __name__ == "__main__":

    FindAllCombination('history')

"""
for i in range(1,100):
    print(i)
for i in enumerate(1,100):
    print(i)