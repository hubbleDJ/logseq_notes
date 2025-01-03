public:: true

- Показать список файлов
  ```bash
  ls
  ls path
  ls -lah # выведет всё содержимое папки с подробной информацией в колонку
  ```
- Показать историю вводимых команд
  ```bash
  history
  ```
- Путь к каталогу, в котором мы сейчас находимся
  ```bash
  pwd
  ```
- Открыть каталог
  ```bash
  cd path
  cd .. # Переход на шаг назад
  ```
- ```bash
  cat name.file # Прочитать файл
  less <file_name> # Читать файл листая его
  ```
- Скопировать наполнение файла
	- ```bash
	  pbcopy < path
	  ```
- Удаление файла/каталога
	- ```bash
	  rm name.file
	  rm <symbols>* # Удалить все файлы, которые начинаются на symbols(* означениет сколько угодно любых символов)
	  rm <symbols>? # Удалить все файлы, которые начинаются на symbols(? означениет один любой символ)
	  rm -rf path # Удалить все без подтверждения
	  rmdir <path_name> # Удалить каталог
	  ```
	- ```bash
	  mv <old_file_name> <new_file_name> # Переименовать файл(точнее переместил его в ту же директорию с новым именем)
	  mv <path_old>/<file_name> <path_new>/<file_name> # Переместить файл
	  cp <path_old>/<file_name> <path_new>/<file_name> # Копирование файла
	  
	  mkdir path_name #Создать каталог
	  ```
- Создать файл
	- ```bash
	  touch <file_name> # Перезапишет дату создания файла, если он есть
	  > <file_name> # Перезапишет файл если он есть
	  ```
- Очистить консоль
  ```bash
  clear
  ```
- Генерация kTab
  ```bash
  /sbin/ipa-getkeytab -P -p 18398782_omega-sbrf-ru -k sc_keytab.keytab - ЛД
  
  C:/"Program Files"/DBeaver/jre/bin/ktab -k C:/Users/18398782/Desktop/gp_keytab -a 18398782@OMEGA.SBRF.RU - GP
  ```
- Информация о пользователе
  ```bash
  id
  ```
- Показать текущую дату и время
  ```bash
  date
  ```
- # Потоки вывода
  
  Стандартная схема вывода
  
  Команда, которая что-то выводит → STDOUT → Терминал
  
  Команда, которая что-то выводит → STDERR → Терминал
  
  STDOUT или 1 - Стандартный поток вывода
  
  STDERR или 2 - Стандартный поток ошибок
- ## Перенаправление потока вывода
  
  Для перенаправления используется символ `>`  или `>>`
  
  При переадресации в файл, сначала происходит создания файла, а потом выполнение самой команды
  
  Перенаправить вывод в файл
  ```bash
  ls -l > <file_name>
  ls -l 1> <file_name> # Перенаправить стандартный вывод в файл
  ls -l 2> <file_name_error> # Перенаправить вывод ошибок в файл
  
  ls -l >> <file_name> # Перенаправит стандартный поток вывода в файл и дозапишет его, если он есть
  
  ls -l <path_name> ./ 2> <file_name> 1> <file_name_error> # Перенаправить оба потока в разные файл
  ```
  
  Склеить 2 файла в один
  ```bash
  cat <file_name1> <file_name2> > <file_name3>
  ```
- ### Перенаправление потоков из программы в программу
  
  Конструкция команды prog1 `|` prog2
  
  Пример перенаправления ls в less
  ```bash
  ls -l <path> | less
  ```
- # Фильтры
  
  ```bash
  head <file_name> # Вывести первые 10 строк файла
  head -n <file_name> # Вывести первые n строк файла
  
  tail <file_name> # Вывести последние 10 строк файла
  tail -n <file_name> # Вывести последние n строк файла
  tail <file_name> -f # Вывести последние 10 строк файла и не закрывать вывод. То есть все новые строки будут выводиться
  ```
  
  ```bash
  grep <word> <file_name> # Показать все строки файла в которых есть <word>
  grep -v <word> <file_name> # Показать все строки файла в которых нет <word>
  
  tail <file_name> -f | grep <word> # Вывести последние 10 строк файла в которых есть <word> и не закрывать вывод. То есть все новые строки с <word> будут выводиться
  ```
  
  Узнать количество строк в файле
  ```bash
  cat <file_name> | wc -l # Узнать количество строк в файле
  wc -l <file_name> # Узнать количество строк в файле
  
  wc <file_name> # Узнать количество слов в файле
  wc -c <file_name> # Узнать количество символов в файле
  ```