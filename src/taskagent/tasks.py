from .file_storage import save_storage, load_storage

tasks: list[dict] = load_storage()


def add(title: str) -> None:
    tasks.append({"title": title, "done": False})
    save_storage(tasks)


def list() -> str:
    result: str = ""

    for i, task in enumerate(tasks):
        result += f"{i}. [{'X' if task['done'] else ' '}] {task['title']}\n"

    return result


def done(idx) -> None:
    tasks[idx]["done"] = True


def help() -> str:
    return ("Это агент для управления задачами\n"
            "Доступные функции:\n"
            "add - добавить задачу\n"
            "list - список задач\n"
            "done - пометить задачу выполненной\n"
            "exit - выход из приложения\n") 

