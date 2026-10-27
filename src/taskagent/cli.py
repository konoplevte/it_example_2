from .tasks import add, done, help, list


def run() -> None:
    while True:
        try:
            command: str = input("> ").lower().strip()

            if command == "add":
                title = input("Input title > ")
                add(title)
            elif command == "list":
                tasks = list()
                print(tasks)
            elif command == "done":
                idx = int(input("Input index > "))
                done(idx)
            elif command == "help":
                print(help())
            elif command == "exit":
                break
            else:
                print("unknown command")
        except IndexError:
            print("Обращение к несуществующему индексу")
        except ValueError:
            print("Ошибка ввода числа")            
