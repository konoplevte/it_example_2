import pytest

from taskagent.tasks import add, list, init_tasks, done, get_tasks, delete_task


@pytest.fixture(autouse=True)
def clear_tasks() -> None:
    init_tasks([])

@pytest.fixture
def add_tasks() -> None:
    init_tasks(
        [
            {"name": "ПРЕСС КАЧАТ", "done": False},
            {"name": "БЕГИТ", "done": False},
            {"name": "АТЖУМАНЯ", "done": False},
        ]
    )

@pytest.mark.parametrize("idx", [0, 1, 2])
def test_mark_task_done(add_tasks, idx):
    done(idx)
    assert get_tasks()[idx]["done"] is True

def test_mark_task_done_invalid_index(add_tasks):
    # Проверка пройдёт, если внутри блока возникнет IndexError
    with pytest.raises(IndexError):
        done(3)

def test_add_task():
    add("ПРЕСС КАЧАТ")
    assert len(get_tasks()) == 1
    assert get_tasks()[0]["name"] == "ПРЕСС КАЧАТ"
    assert get_tasks()[0]["done"] is False


def test_list_task():

    add("ПРЕСС КАЧАТ")
    assert len(get_tasks()) == 1
    assert list() == "0. [ ] ПРЕСС КАЧАТ\n"

def test_delete_task(add_tasks):
    task = delete_task(1)
    current_tasks = get_tasks()
    assert len(current_tasks) == 2
    assert current_tasks[0]["name"] == "ПРЕСС КАЧАТ"
    assert current_tasks[1]["name"] == "АТЖУМАНЯ"

    assert task == {"name": "БЕГИТ", "done": False}
   