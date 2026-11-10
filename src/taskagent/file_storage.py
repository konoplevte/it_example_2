from pathlib import Path

STORAGE_FILE = Path("data", "tasks.txt")
STORAGE_FILE.parent.mkdir(parents=True, exist_ok=True)

def save_storage(data: list[dict]) -> None:
    with STORAGE_FILE.open("w", encoding="utf-8") as file:
        file.write(str(data))

def load_storage() -> list[dict]:
    pass