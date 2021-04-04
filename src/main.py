import random
import string


def randstr() -> str:
    length = random.randint(6, 100)
    letters = string.ascii_lowercase
    
    result = ''
    for i in range(length):
        result += random.choice(letters)
    
    return result


def count_unique(string: str):
    counts = dict()
    for symbol in string:
        counts[symbol] = counts.get(symbol, 0) + 1
    
    return len(counts)
    

if __name__ == '__main__':
    for i in range(10):
        tmp = randstr()
        print(tmp)
        print(count_unique(tmp))
