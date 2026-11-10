
_tasks: list[dict] = []

def init_tasks(tasks: list[dict]) -> None:
    global _tasks
    _tasks = tasks

def get_tasks() -> list[dict]:
    return _tasks

def add(title: str) -> None:
    _tasks.append({"name": title, "done": False})


def list() -> str:
    result: str = ""

    for i, task in enumerate(_tasks):
        result += f"{i}. [{'X' if task['done'] else ' '}] {task['name']}\n"

    return result


def done(idx) -> None:
    _tasks[idx]["done"] = True

def delete_task(idx) -> dict | None:
    if idx < 0:
        raise IndexError("Индекс меньше 0")

    try:
        return _tasks.pop(idx)
    except IndexError:
        return None

def help() -> str:
    return ("Это агент для управления задачами\n"
            "Доступные функции:\n"
            "add - добавить задачу\n"
            "list - список задач\n"
            "done - пометить задачу выполненной\n"
            "exit - выход из приложения\n") 

