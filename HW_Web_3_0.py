import time
import random, 


def factorize(*numbers):

    
    result = []
    for number in numbers:
        divisor = []
        for i in range(1, number + 1):
            if number % i == 0:
                divisor.append(i)
        result.append(divisor)
    return result


start_time = time.time()
a, b, c, d = factorize(128, 255, 99999, 10651060)
end_time = time.time()

print(f"Синхронна версія - {end_time - start_time:} секунд.")
print(a)
print(b)
print(c)
print(d)

