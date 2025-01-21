# shutil.make_archive(base_name, format, root_dir=None, base_dir=None)

import shutil

# Створення ZIP-архіву з вмістом директорії 'my_folder'
shutil.make_archive('example', 'zip', root_dir='/Users/lidiiachernysh/Documents/personal/Learning_Python/My_repo/learning_repo/work_with_files/')


# Розпакування ZIP-архіву в певну директорію
shutil.unpack_archive('example.zip', '/Users/lidiiachernysh/Documents/personal/Learning_Python/My_repo/learning_repo')



# Копіюємо файл
source_file = '/Users/lidiiachernysh/Documents/personal/Learning_Python/My_repo/learning_repo/work_with_files/file_archive.py'
destination_dir = '/Users/lidiiachernysh/Documents/personal/Learning_Python/My_repo/test'
shutil.copy(source_file, destination_dir)

# Копіюємо всю директорію
source_dir = '/Users/lidiiachernysh/Documents/personal/Learning_Python/My_repo/learning_repo'
destination_dir = '/Users/lidiiachernysh/Documents/personal/Learning_Python/My_repo/test2'
shutil.copytree(source_dir, destination_dir)


# Відкриття текстового файлу з явним вказівкам UTF-8 кодування
with open('example.txt', 'r', encoding='utf-8') as file:
    content = file.read()
    print(content)
