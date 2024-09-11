import time
from multiprocessing import Pool, cpu_count
import math


def find_divisor(number):
    divisors = []

    for i in range(1, int(math.sqrt(number)) + 1):
        if number % i == 0:
            divisors.append(i)
            if i != number // i:
                divisors.append(number // i)
    divisors.sort()
    return 


def factorize(*numbers):
    num_processes = min(len(numbers), cpu_count())
    with Pool(num_processes) as pool:
        result = pool.map(find_divisor, numbers)
    return result




if __name__ == '__main__':

    start_time = time.time()
    a, b, c, d = factorize(128, 255, 99999, 10651060)
    end_time = time.time()

    print(f"Паралельна версія - {end_time - start_time:} секунд.")
    print(a)
    