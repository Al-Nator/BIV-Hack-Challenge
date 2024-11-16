import logging
import dill
import sys
import os

# Настраиваем логирование
logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s:%(message)s")

def load_model(model_path):
    """
    Загружает классификационную модель из файла.

    Параметры:
    model_path (str): Путь к файлу с сохраненной моделью.

    Возвращает:
    cls_model: Загруженная модель классификации.
    """
    if not os.path.exists(model_path):
        logging.error(f"Файл модели не найден по пути: {model_path}")
        sys.exit(1)
    try:
        with open(model_path, "rb") as f:
            cls_model = dill.load(f)
        logging.info("Модель успешно загружена")
        return cls_model
    except Exception as e:
        logging.error(f"Ошибка при загрузке модели: {e}")
        sys.exit(1)

def load_vectorizer(vectorizer_path):
    """
    Загружает векторизатор из файла.

    Параметры:
    vectorizer_path (str): Путь к файлу с сохраненным векторизатором.

    Возвращает:
    vectorizer: Загруженный векторизатор.
    """
    if not os.path.exists(vectorizer_path):
        logging.error(f"Файл векторизатора не найден по пути: {vectorizer_path}")
        sys.exit(1)
    try:
        with open(vectorizer_path, "rb") as f:
            vectorizer = dill.load(f)
        logging.info("Векторизатор успешно загружен")
        return vectorizer
    except Exception as e:
        logging.error(f"Ошибка при загрузке векторизатора: {e}")
        sys.exit(1)