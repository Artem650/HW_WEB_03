import time
from multiprocessing import Pool, cpu_count

def factorize_single(el):
    factors = [i for i in range(1, el + 1) if el % i == 0]
    return factors

def factorize_parallel(*numbers):
    pool = Pool(processes=cpu_count())
    results = pool.map(factorize_single, numbers)
    pool.close()
    pool.join()
    return results

if __name__ == "__main__":
    numbers = [128, 255, 99999, 10651060]
    start_time = time.time()
    results = factorize_parallel(*numbers)
    end_time = time.time()
    realization_time_parallel = end_time - start_time


    for i, result in enumerate(results):
        print(f"Factors for {numbers[i]}: {result}")

    print("Realization time:", realization_time_parallel)