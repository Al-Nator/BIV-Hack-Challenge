from bisect import bisect_left
import pandas as pd
import logging

# Настраиваем логирование
logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s:%(message)s")

def load_words_from_file(file_path):
    """
    Загружает слова из текстового файла с использованием бинарного поиска.

    Параметры:
    file_path (str): Путь к текстовому файлу с перечнем слов.

    Возвращает:
    list: Отсортированный список слов в нижнем регистре. Если возникает ошибка кодировки, возвращает пустой список.
    """
    try:
        with open(file_path, 'r', encoding='cp1251') as file:
            words = file.read().splitlines()
    except UnicodeDecodeError:
        logging.info("Ошибка кодировки при чтении файла")
        return []
    
    # Преобразуем все слова в нижний регистр для корректного сравнения
    words = [word.lower() for word in words if word.isalpha()]
    return sorted(words)  # Явно сортируем список

def binary_search(word_list, word):
    """
    Выполняет бинарный поиск слова в отсортированном списке.

    Параметры:
    word_list (list): Отсортированный список слов.
    word (str): Слово для поиска.

    Возвращает:
    bool: True, если слово найдено в списке, иначе False.
    """
    index = bisect_left(word_list, word)
    return index < len(word_list) and word_list[index] == word

def is_transposition_typo(word, dictionary):
    """
    Проверяет, является ли слово результатом перестановки двух или трёх соседних букв и возвращает исправленное слово.

    Параметры:
    word (str): Исходное слово для проверки.
    dictionary (list): Отсортированный список слов для поиска.

    Возвращает:
    str или None: Исправленное слово, если найдено соответствие в словаре, иначе None.
    """
    word_length = len(word)
    
    # Проверка перестановок длины 2 (соседние буквы)
    for i in range(word_length - 1):
        transposed_word = list(word)
        transposed_word[i], transposed_word[i + 1] = transposed_word[i + 1], transposed_word[i]
        transposed_word = ''.join(transposed_word)
        
        if binary_search(dictionary, transposed_word):
            logging.info(f"Исправлено '{word}' на '{transposed_word}' (перестановка двух букв)")
            return transposed_word
    
    # Проверка перестановок длины 3 (три соседние буквы)
    for i in range(word_length - 2):
        # Перестановка: ABC -> BAC
        transposed_word = list(word)
        transposed_word[i], transposed_word[i + 1], transposed_word[i + 2] = transposed_word[i + 1], transposed_word[i], transposed_word[i + 2]
        transposed_word_bac = ''.join(transposed_word)
        
        if binary_search(dictionary, transposed_word_bac):
            logging.info(f"Исправлено '{word}' на '{transposed_word_bac}' (перестановка трех букв BAC)")
            return transposed_word_bac
        
        # Перестановка: ABC -> ACB
        transposed_word = list(word)
        transposed_word[i], transposed_word[i + 1], transposed_word[i + 2] = transposed_word[i], transposed_word[i + 2], transposed_word[i + 1]
        transposed_word_acb = ''.join(transposed_word)
        
        if binary_search(dictionary, transposed_word_acb):
            logging.info(f"Исправлено '{word}' на '{transposed_word_acb}' (перестановка трех букв ACB)")
            return transposed_word_acb

    return None

def custom_tokenizer(text, dictionary):
    """
    Токенизирует текст и исправляет опечатки путем поиска перестановок соседних букв.

    Параметры:
    text (str): Исходный текст для токенизации и исправления.

    Возвращает:
    str: Текст с исправленными словами, если были найдены опечатки.
    """
    words = text.split()
    corrected_words = []
    for word in words:
        lower_word = word.lower()
        if binary_search(dictionary, lower_word):
            corrected_words.append(word)
        elif len(lower_word) > 3:
            # Ищем исправление с перестановками соседних символов (длиной 2 и 3)
            corrected_word = is_transposition_typo(lower_word, dictionary)
            if corrected_word:
                corrected_words.append(corrected_word)
            else:
                corrected_words.append(word)
        else:
            corrected_words.append(word)
    return ' '.join(corrected_words)