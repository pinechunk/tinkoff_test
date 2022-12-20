import argparse
import difflib

def evaluate_similarity(text1, text2):
    '''Чтобы запустить скрипт, нужно ввести в командной строке — python maim.py input_file output_file,
    где input_file и output_file — пути к файлам формата .txt в общей папке.
    В файле input попарно прописать пути к файлам для поиска плагиата.
    В файле output будет результат.'''

    # Создаю функцию для сравнения текста
    matcher = difflib.SequenceMatcher(None, text1, text2)

    # Вычисляю сходство как отношение совпадающих символов
    # к общему количеству символов в более длинном тексте
    similarity = matcher.ratio()

    return similarity


if __name__ == '__main__':
    #
    parser = argparse.ArgumentParser()
    parser.add_argument('input_file', help='file with a list of document pairs')
    parser.add_argument('output_file', help='path to the output file')
    args = parser.parse_args()

    with open(args.input_file, 'r') as input_file:
        with open(args.output_file, 'w') as output_file:
            for line in input_file:
                # Разделить файл на две части
                file1, file2 = line.strip().split()

                # Вывод пути к файлам в консоль
                print(file1)
                print(file2)

                # Чтение файла
                with open(file1, 'r', encoding='utf8') as f1:
                    text1 = f1.read()
                with open(file2, 'r', encoding='utf8') as f2:
                    text2 = f2.read()

                # Оценка сходства текстов
                similarity = evaluate_similarity(text1, text2)

                # Запись результата в файл output
                output_file.write(f'{similarity}\n')
