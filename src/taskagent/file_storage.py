from pathlib import Path
import json

_storage_path = Path("data", "tasks.json")

def init_storage(path: Path) -> None:
    global _storage_path
    _storage_path = path
    _storage_path.parent.mkdir(parents=True, exist_ok=True)

def save_storage(data: list[dict]) -> None:
    with _storage_path.open("w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

def load_storage() -> list[dict]:
    try:
        with _storage_path.open("r", encoding="utf-8") as file:
            # load() десериализует JSON из файла обратно в объект Python.
            return json.load(file)
    except FileNotFoundError:
        return []