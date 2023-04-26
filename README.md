# docx_replacer
В этом примере мы создаем объект парсера с помощью argparse.ArgumentParser и добавляем три аргумента командной строки: directory, old_text и new_text. Затем мы парсим аргументы с помощью parser.parse_args() и передаем их в функцию replace_text_in_docx.

Теперь вы можете запустить программу из командной строки, передав значения параметров для directory, old_text и new_text, например:

python script.py /path/to/directory текст_1 текст_2
