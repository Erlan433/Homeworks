import os
import sys
import platform


# Сохраняем результаты работы функций в переменные
system_name = platform.system()
system_version = platform.release()
computer_name = platform.node()
architecture = platform.machine()
processor = platform.processor()
python_version = platform.python_version()
current_directory = os.getcwd()
process_id = os.getpid()
cpu_count = os.cpu_count()
python_platform = sys.platform


# Добавляем полученные данные в список
system_info = [
    system_name,
    system_version,
    computer_name,
    architecture,
    processor,
    python_version,
    current_directory,
    process_id,
    cpu_count,
    python_platform
]


while True:

    # Вывод меню через sys.stdout
    sys.stdout.write("\n===== ДИАГНОСТИКА СИСТЕМЫ =====\n")
    sys.stdout.write("1. Операционная система\n")
    sys.stdout.write("2. Версия операционной системы\n")
    sys.stdout.write("3. Имя компьютера\n")
    sys.stdout.write("4. Архитектура компьютера\n")
    sys.stdout.write("5. Процессор\n")
    sys.stdout.write("6. Версия Python\n")
    sys.stdout.write("7. Текущая папка программы\n")
    sys.stdout.write("8. ID процесса\n")
    sys.stdout.write("9. Количество процессоров\n")
    sys.stdout.write("10. Платформа Python\n")
    sys.stdout.write("0. Выход\n")

    sys.stdout.write("\nВыберите пункт: ")
    sys.stdout.flush()

    # Получаем ввод через sys.stdin
    choice = sys.stdin.readline().strip()

    if choice == "1":
        sys.stdout.write("Операционная система: " + str(system_info[0]) + "\n")

    elif choice == "2":
        sys.stdout.write(
            "Версия операционной системы: "
            + str(system_info[1])
            + "\n"
        )

    elif choice == "3":
        sys.stdout.write("Имя компьютера: " + str(system_info[2]) + "\n")

    elif choice == "4":
        sys.stdout.write("Архитектура: " + str(system_info[3]) + "\n")

    elif choice == "5":
        sys.stdout.write("Процессор: " + str(system_info[4]) + "\n")

    elif choice == "6":
        sys.stdout.write("Версия Python: " + str(system_info[5]) + "\n")

    elif choice == "7":
        sys.stdout.write(
            "Текущая папка: "
            + str(system_info[6])
            + "\n"
        )

    elif choice == "8":
        sys.stdout.write("ID процесса: " + str(system_info[7]) + "\n")

    elif choice == "9":
        sys.stdout.write(
            "Количество процессоров: "
            + str(system_info[8])
            + "\n"
        )

    elif choice == "10":
        sys.stdout.write(
            "Платформа Python: "
            + str(system_info[9])
            + "\n"
        )

    elif choice == "0":
        sys.stdout.write("Программа завершена.\n")
        break

    else:
        sys.stdout.write("Такого пункта нет. Попробуйте снова.\n")