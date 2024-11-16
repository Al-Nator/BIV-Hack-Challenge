from src.predictor import predict
import argparse
import logging
import os

# Настраиваем логирование
logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s:%(message)s")

if __name__ == "__main__":
    # Парсинг аргументов командной строки
    parser = argparse.ArgumentParser(description="Проект по классификации описаний платежей по категориям от команды MMG")
    parser.add_argument("--model", type=str, default="./src/models/classifier.dill", help="Путь к файлу модели")
    parser.add_argument("--vectorizer", type=str, default="./src/models/tf-idf-vectorizer.dill", help="Путь к файлу векторизатора")
    parser.add_argument("--input", type=str, default="./input/payments_main.tsv", help="Путь к входному TSV файлу с данными")
    parser.add_argument("--output", type=str, default="./output/predictions.tsv", help="Путь к выходному TSV файлу с предсказаниями")

    # Парсим аргументы
    args = parser.parse_args()
    # Создаем выходную директорию, если она не существует
    os.makedirs(os.path.dirname(args.output), exist_ok=True)

    # Выполняем предсказание
    data_final = predict(args.model, args.vectorizer, args.input)

    # Сохраняем результат в TSV файл без индексов и заголовков
    data_final.to_csv(args.output, sep="\t", index=False, header=False)
    logging.info(f"Результаты сохранены в файл \"{args.output}\"")