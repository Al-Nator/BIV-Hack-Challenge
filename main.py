from src.predictor import predict
import argparse
import logging
import os

# Настраиваем логирование
logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s:%(message)s")

if __name__ == "__main__":
    # Парсинг аргументов командной строки
    parser = argparse.ArgumentParser(description="Проект по классификации описаний платежей по категориям от команды MMG")
    arguments = [
        ("--model", "./src/models/classifier.dill", "Путь к файлу модели"),
        ("--vectorizer", "./src/models/tf-idf-vectorizer.dill", "Путь к файлу векторизатора"),
        ("--input", "./input/payments_main.tsv", "Путь к входному TSV файлу с данными"),
        ("--output", "./output/predictions.tsv", "Путь к выходному TSV файлу с предсказаниями")
    ]
    for argument in arguments:
        parser.add_argument(argument[0], type=str, default=argument[1], help=argument[2])

    # Парсим аргументы
    args = parser.parse_args()
    # Создаем выходную директорию, если она не существует
    os.makedirs(os.path.dirname(args.output), exist_ok=True)

    # Выполняем предсказание
    data_final = predict(args.model, args.vectorizer, args.input)

    # Сохраняем результат в TSV файл без индексов и заголовков
    data_final.to_csv(args.output, sep="\t", index=False, header=False)
    logging.info(f"Результаты сохранены в файл \"{args.output}\"")