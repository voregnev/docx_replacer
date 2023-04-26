import os
import docx
import argparse

def replace_text_in_docx(directory, old_text, new_text):
    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)
        if os.path.isdir(filepath):
            replace_text_in_docx(filepath, old_text, new_text)
        elif filename.endswith('.docx'):
            doc = docx.Document(filepath)
            for section in doc.sections:
                header = section.header
                for paragraph in header.paragraphs:
                    if old_text in paragraph.text:
                        paragraph.text = paragraph.text.replace(old_text, new_text)
            doc.save(filepath)

if __name__ == '__main__':
    # Создаем объект парсера и добавляем аргументы командной строки
    parser = argparse.ArgumentParser(description='Replace text in all .docx files in directory')
    parser.add_argument('directory', type=str, help='Directory to search for .docx files')
    parser.add_argument('old_text', type=str, help='Text to be replaced')
    parser.add_argument('new_text', type=str, help='New text to replace with')

    # Парсим аргументы командной строки
    args = parser.parse_args()

    # Вызываем функцию для замены текста в .docx файлах
    replace_text_in_docx(args.directory, args.old_text, args.new_text)
