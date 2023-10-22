import time

def show_primes(number):
    for i in range(2, number):
        if (number % i == 0):
            return 0
    return 1

def main():
    primes = []
    for i in range(1, 100):
        if (show_primes(i) == 1):
            primes.append(i)
    print(primes)

if __name__ == "__main__":
    start_time = time.time()
    main()
    print("\nFinished in:", time.time() - start_time)