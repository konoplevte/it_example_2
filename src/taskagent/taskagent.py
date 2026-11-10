from pathlib import Path

from .cli import run
from .file_storage import init_storage, load_storage, save_storage
from .tasks import get_tasks, init_tasks


def main() -> None:
    init_storage(Path("data", "tasks.json"))
    loaded_tasks = load_storage()
    init_tasks(loaded_tasks)
    run()
    save_storage(get_tasks())


if __name__ == "__main__":
    main()
