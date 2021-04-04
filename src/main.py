import random
import string

def randstr() -> str:
    length = random.randint(6, 30)
    letters = string.ascii_lowercase
    
    result = ''
    for i in range(length):
        result += random.choice(letters)
    
    return result

if __name__ == '__main__':
    for i in range(10):
        print(randstr())
