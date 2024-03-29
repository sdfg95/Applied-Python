import threading
import multiprocessing
import time


def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def run_fibonacci(n):
    start_time = time.time()
    result = fibonacci(n)
    end_time = time.time()
    return end_time - start_time


def run_with_threads(n, num_threads):
    start_time = time.time()
    threads = []
    for _ in range(num_threads):
        t = threading.Thread(target=run_fibonacci, args=(n,))
        threads.append(t)
        t.start()
    for thread in threads:
        thread.join()
    end_time = time.time()
    return end_time - start_time


def run_with_processes(n, num_processes):
    start_time = time.time()
    processes = []
    for _ in range(num_processes):
        p = multiprocessing.Process(target=run_fibonacci, args=(n,))
        processes.append(p)
        p.start()
    for process in processes:
        process.join()
    end_time = time.time()
    return end_time - start_time


def main():
    n = 21
    num_runs = 10
    num_threads = 10
    num_processes = 10

    sync_times = [run_fibonacci(n) for _ in range(num_runs)]

    thread_times = [run_with_threads(n, num_threads) for _ in range(num_runs)]

    process_times = [run_with_processes(n, num_processes) for _ in range(num_runs)]

    with open("../../artifacts/4.1/results.txt", "w") as f:
        f.write("Synchronous execution:\n")
        f.write(f"Average time: {sum(sync_times) / num_runs}\n")
        f.write("Thread execution:\n")
        f.write(f"Average time: {sum(thread_times) / num_runs}\n")
        f.write("Process execution:\n")
        f.write(f"Average time: {sum(process_times) / num_runs}\n")


if __name__ == "__main__":
    main()
