import multiprocessing
import time

def burn():
    # Infinite loop to fully load a core
    while True:
        pass

if __name__ == "__main__":
    num_cores = multiprocessing.cpu_count()
    print(f"Starting CPU stress test on {num_cores} cores...")

    processes = []
    for _ in range(num_cores):
        p = multiprocessing.Process(target=burn)
        p.start()
        processes.append(p)

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nStopping stress test...")
        for p in processes:
            p.terminate()
        for p in processes:
            p.join()
