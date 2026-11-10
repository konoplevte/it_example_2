from pathlib import Path
import json

STORAGE_FILE = Path("data", "tasks.json")
STORAGE_FILE.parent.mkdir(parents=True, exist_ok=True)

def save_storage(data: list[dict]) -> None:
    with STORAGE_FILE.open("w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

def load_storage() -> list[dict]:
    try:
        with STORAGE_FILE.open("r", encoding="utf-8") as file:
            # load() десериализует JSON из файла обратно в объект Python.
            return json.load(file)
    except FileNotFoundError:
        return []