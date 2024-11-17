from src.correction import load_words_from_file, custom_tokenizer
from src.model_loader import load_model, load_vectorizer
from src.data_loader import load_data
import logging
import sys

def predict(model_path, vectorizer_path, dictionary_file_path, file_path):
    """
    Загружает модель, векторизатор и данные, затем предсказывает категории для текстовых данных.

    Параметры:
    model_path (str): Путь к файлу с моделью.
    vectorizer_path (str): Путь к файлу с векторизатором.
    file_path (str): Путь к файлу с данными.

    Возвращает:
    DataFrame: Данные с предсказанными категориями.
    """
    cls_model = load_model(model_path)
    vectorizer = load_vectorizer(vectorizer_path)
    data = load_data(file_path)

    # Проверяем наличие столбца "text" в данных
    if "text" not in data.columns:
        logging.error("В данных отсутствует столбец \"text\"")
        sys.exit(1)

    # Исправление опечаток
    dictionary = load_words_from_file(dictionary_file_path)
    data['text'] = data['text'].apply(lambda x: custom_tokenizer(x, dictionary))

    # Преобразуем текстовые данные с помощью векторизатора
    X_test = vectorizer.transform(data["text"])
    # Предсказываем категории
    data["predicted_category"] = cls_model.predict(X_test)

    logging.info("Предсказание завершено")
    return data[["index", "predicted_category"]]