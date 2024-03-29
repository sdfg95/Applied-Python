import math
import concurrent.futures
import logging
import os
import time

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s',
                    filename='../../artifacts/4.2/logs.txt')


def integrate_threaded(f, a, b, *, n_jobs=1, n_iter=10000):
    acc = 0
    step = (b - a) / n_iter
    with concurrent.futures.ThreadPoolExecutor(max_workers=n_jobs) as executor:
        futures = [executor.submit(f, a + i * step) for i in range(n_iter)]
        for future in concurrent.futures.as_completed(futures):
            acc += future.result() * step
            logging.info(f'Threaded task completed')
    return acc


def integrate_multiprocess(f, a, b, *, n_jobs=1, n_iter=10000):
    acc = 0
    step = (b - a) / n_iter
    with concurrent.futures.ProcessPoolExecutor(max_workers=n_jobs) as executor:
        futures = [executor.submit(f, a + i * step) for i in range(n_iter)]
        for future in concurrent.futures.as_completed(futures):
            acc += future.result() * step
            logging.info(f'Multiprocess task completed: {future}')
    return acc


def compare_execution_time(n_jobs_values):
    threaded_results = {}
    process_results = {}

    for n_jobs in n_jobs_values:
        start_time = time.time()
        threaded_result = integrate_threaded(math.cos, 0, math.pi / 2, n_jobs=n_jobs)
        end_time = time.time()
        threaded_execution_time = end_time - start_time
        threaded_results[n_jobs] = threaded_execution_time

        start_time = time.time()
        process_result = integrate_multiprocess(math.cos, 0, math.pi / 2, n_jobs=n_jobs)
        end_time = time.time()
        process_execution_time = end_time - start_time
        process_results[n_jobs] = process_execution_time

    with open(f'../../artifacts/4.2/results.txt', 'w') as f:
        f.write(f"Results:\n")
        f.write(f"Threaded Results:\n")
        for n_jobs, execution_time in threaded_results.items():
            f.write(f"n_jobs: {n_jobs}, Execution time: {execution_time}\n")

        f.write(f"Process Results:\n")
        for n_jobs, execution_time in process_results.items():
            f.write(f"n_jobs: {n_jobs}, Execution time: {execution_time}\n")


if __name__ == "__main__":
    n_jobs_values = list(range(1, os.cpu_count() * 2 + 1))
    compare_execution_time(n_jobs_values)
