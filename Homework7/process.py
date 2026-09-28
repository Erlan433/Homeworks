import os
import time
from multiprocessing import Process


def process_one():
    print(f"Процесс 1 запущен. ID: {os.getpid()}")
    time.sleep(2)
    print("Процесс 1 завершил работу.")


def process_two():
    print(f"Процесс 2 запущен. ID: {os.getpid()}")
    time.sleep(3)
    print("Процесс 2 завершил работу.")


def process_three():
    print(f"Процесс 3 запущен. ID: {os.getpid()}")
    time.sleep(1)
    print("Процесс 3 завершил работу.")


def process_four():
    print(f"Процесс 4 запущен. ID: {os.getpid()}")
    time.sleep(4)
    print("Процесс 4 завершил работу.")


if __name__ == "__main__":
    print(f"Главный процесс. ID: {os.getpid()}\n")

    p1 = Process(target=process_one)
    p2 = Process(target=process_two)
    p3 = Process(target=process_three)
    p4 = Process(target=process_four)

    p1.start()
    print(f"Запущен процесс 1, его ID: {p1.pid}")

    p2.start()
    print(f"Запущен процесс 2, его ID: {p2.pid}")

    p3.start()
    print(f"Запущен процесс 3, его ID: {p3.pid}")

    p4.start()
    print(f"Запущен процесс 4, его ID: {p4.pid}")

    p1.join()
    p2.join()
    p3.join()
    p4.join()

    print("\nВсе процессы завершены.")
