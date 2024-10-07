import threading
from time import sleep, time

def write_words(word_count, file_name):
    with open(file_name, 'w') as f:
        for i in range(1, word_count + 1):
            f.write(f"Какое-то слово № {i}\n")
            sleep(0.1)
    print(f"Завершилась запись в файл {file_name}")

def run_write_operations():
    start_time = time()

    write_words(10, 'example1.txt')
    write_words(30, 'example2.txt')
    write_words(200, 'example3.txt')
    write_words(100, 'example4.txt')

    end_time = time()
    print(f"Работа потоков {end_time - start_time:.6f} секунд")

    start_time_threads = time()

    threads = []
    thread_params = [(10, 'example5.txt'), (30, 'example6.txt'), (200, 'exemple7.txt'), (100, 'exemple8.txt'), ]

    for params in thread_params:
        thread = threading.Thread(target=write_words, args=params)
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    end_time_threads = time()
    print(f"Работа потоков {end_time_threads - start_time_threads:.6f} секунд")

if __name__ == "__main__":
    run_write_operations()