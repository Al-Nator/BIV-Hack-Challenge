import pandas as pd
import logging
import sys
import os

# Настраиваем логирование
logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s:%(message)s")

def load_data(file_path):
    """
    Загружает данные из TSV файла и переименовывает столбцы.

    Параметры:
    file_path (str): Путь к TSV файлу с данными.

    Возвращает:
    data (DataFrame): Загруженные и обработанные данные.
    """
    if not os.path.exists(file_path):
        logging.error(f"Файл данных не найден по пути: {file_path}")
        sys.exit(1)
    try:
        data = pd.read_csv(file_path, sep="\t", header=None)
        data = data.rename(columns={0: "index", 1: "date", 2: "amount", 3: "text"})
        logging.info("Данные успешно загружены")
        return data
    except Exception as e:
        logging.error(f"Ошибка при загрузке данных: {e}")
        sys.exit(1)