# BIV Hack Challenge – Команда MMG
Кейс Автоматизация разбора платежей

## Описание задачи
Создать модель, способную классифицировать назначения платежей на основе введенного текста. Обучить модель на реальных данных и обеспечить высокую точность в определении категории платежа.

## Описание проекта
Проект разработан для автоматической классификации описаний платежей по категориям. Использует машинное обучение для анализа текстовых описаний транзакций и их категоризации с высокой скоростью.

## Состав команды
* **Денис Маликов** – Капитан, DA
* **Артём Таратин** – DS
* **Даниил Аль-Натор** – DS
* **Илья Обухов** – DE

## Зависимости
* scikit-learn – построение моделей машинного обучения
* pandas, numpy – работа с данными
* dill – сохранение и загрузка обученных моделей

## Загрузка
```bash
git clone https://github.com/kekwak/BIV-Hack-Challenge.git && cd BIV-Hack-Challenge
```

## Запуск в контейнере
```bash
docker compose up --build
```

## Запуск в локальной среде
С помощью `python3.11`
```bash
python3 -m venv .venv
source ".venv/bin/activate"
pip install -r requirements.txt
python3 main.py
```

## Особые аргументы
```bash
python3 main.py --help
```

```bash
usage: main.py [-h] [--model MODEL] [--vectorizer VECTORIZER] [--input INPUT] [--output OUTPUT]

Проект по классификации описаний платежей по категориям от команды MMG

options:
  -h, --help                Показывает справочное сообщение и выходит
  --model MODEL             Путь к файлу модели
  --vectorizer VECTORIZER   Путь к файлу векторизатора
  --input INPUT             Путь к входному TSV файлу с данными
  --output OUTPUT           Путь к выходному TSV файлу с предсказаниями
```

## Структура проекта
```
.
├── src <------------------------ Исходный код проекта
│   ├── models <----------------- Обученные модели
│   ├── data_loader.py <--------- Загрузка данных
│   ├── model_loader.py <-------- Загрузка моделей
│   └── predictor.py <----------- Логика предсказаний
├── input <---------------------- Входные данные
│   ├── payments_main.tsv <------ Основные платежные данные 25k
│   └── payments_training.tsv <-- Обучающие данными ½k
├── output <--------------------- Результаты предсказаний
├── notebooks <------------------ Jupyter ноутбуки
├── main.py <-------------------- Главный исполняемый файл проекта
├── README.md <------------------ Описание
├── docker-compose.yaml <-------- Конфигурационный файл для Docker Compose
├── Dockerfile <----------------- Файл для сборки Docker-образа
└── requirements.txt <----------- Список зависимостей проекта
```
