import os

from git import Repo
from pathlib import Path

BASE_DIR = Path(Path(__file__).resolve().parent)
PAGES_DIR = Path(BASE_DIR, 'pages')
ASSETS_DIR = Path(BASE_DIR, 'assets')

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

git_push(
    'Коммит первых файлов',
    public_files
)

