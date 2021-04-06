import random
import string
import threading
import queue
import time
import argparse


def randstr() -> str:
    length = random.randint(6, 100)
    letters = string.ascii_lowercase
    
    result = ''
    for i in range(length):
        result += random.choice(letters)
    
    return result


def count_unique(string: str) -> int:
    counts = dict()
    for symbol in string:
        counts[symbol] = counts.get(symbol, 0) + 1
    
    return (string, len(counts))
    

def producer(q: queue.Queue, cond: threading.Condition, n: int):
    while True:
        time.sleep(n)
        cond.acquire()
        try:
            q.put(randstr())
            print("String produced by Producer with id: " + str(threading.get_ident()))
            cond.notify()
        finally:
            cond.release()


def consumer(q: queue.Queue, cond: threading.Condition):
    cond.acquire()
    while True:
        try:
            tmp = count_unique(q.get_nowait())
            print("Answer: " + str(tmp[1]) + " for string: " + tmp[0])
        except:
            value = cond.wait()
            if value:
                print("Notification for Consumer with id: " + str(threading.get_ident()))
                continue
            else:
                print("Timeout")
                break

    cond.release()


if __name__ == '__main__':
    q = queue.Queue()
    cond = threading.Condition()
    
    parser = argparse.ArgumentParser()
    parser.add_argument("--producers", help="number of producers", type=int)
    parser.add_argument("--consumers", help="number of consumers", type=int)
    parser.add_argument("--time", help="time (seconds) for producer to wait", type=int)
    args = parser.parse_args()

    for i in range(args.producers):
        threading.Thread(target=producer, args=(q,cond, args.time,)).start()
    
    for i in range(args.consumers):
        threading.Thread(target=consumer, args=(q,cond,)).start()