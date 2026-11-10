from taskagent.file_storage import init_storage, load_storage, save_storage


def test_storage(tmp_path):
    # Инициализация хранилища с использованием временного пути
    test_file = tmp_path / "test_tasks.json"
    init_storage(test_file)

    # Проверка, что файл не существует до сохранения
    assert not test_file.exists()

    # Сохранение данных в хранилище
    data_to_save = [{"name": "Test Task", "done": False}]
    save_storage(data_to_save)

    # Проверка, что файл был создан
    assert test_file.exists()

    # Загрузка данных из хранилища
    loaded_data = load_storage()
    assert loaded_data == data_to_save

    # Очистка хранилища и проверка загрузки пустого списка
    save_storage([])
    loaded_empty_data = load_storage()
    assert loaded_empty_data == []
