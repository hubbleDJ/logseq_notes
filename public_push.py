import os
import json

from git import Repo
from pathlib import Path

BASE_DIR = Path(Path(__file__).resolve().parent)
PAGES_DIR = Path(BASE_DIR, 'pages')
ASSETS_DIR = Path(BASE_DIR, 'assets')
PUBLIC_FILES_PATH = Path(BASE_DIR, 'public_files.json')

def get_old_public_files():
    with open(PUBLIC_FILES_PATH, 'r') as f:
        return json.load(f)


def get_remote_files(new_public_files: list[str], old_public_files: list[str]):
    return list(set(old_public_files) - set(new_public_files))


def get_public_pages():
    public_notes = []
    for file in os.listdir(PAGES_DIR):
        if file.split('.')[-1] == 'md':
            with open(Path(PAGES_DIR, file), 'r') as f:
                lines = f.readlines()
                if len(lines) > 0 and 'public:: true' in lines[0]:
                    public_notes.append(str(Path('pages', file)))

    return public_notes

def git_push(commit_message: str, files_to_push: list[str]=[], files_to_remove: list[str]=[]):
    # Открываем репозиторий
    repo = Repo(BASE_DIR)

    # Проверяем, что это действительно репозиторий
    if not repo.bare:
        try:
            if len(files_to_push) > 0:
                repo.index.add(files_to_push)
            if len(files_to_remove) > 0:
                epo.index.remove(files_to_remove)
            if len(files_to_push) == 0 and len(files_to_remove) == 0:
                print('Нет файлов для изменения')
                exit()
            repo.index.commit(commit_message)

            origin = repo.remote(name='origin')
            origin.push()

            print('Файлы успешно добавлены и запушены!')
        except Exception as e:
            print(f'Ошибка: {e}')
    else:
        print("Не удалось открыть репозиторий.")

public_files = ['public_push.py'] + get_public_pages()
print(get_remote_files(
    public_files,
    get_old_public_files()
))

git_push(
    'Коммит первых файлов',
    public_files
)

