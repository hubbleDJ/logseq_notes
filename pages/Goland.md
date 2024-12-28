public:: true

- ## Библиотеки
	- #[[math goland]]
	- #[[strconv goland]]
	-
- Команды выполнения
	- ```bash
	  // Запуск
	  go run main.go
	  
	  // Форматирование
	  go fmt main.go
	  
	  // Компиляция
	  go main.go
	  
	  // Запуск компилированного файла
	  ./main
	  
	  // Посмотреть версию go
	  go version
	  ```
- Комментарии
	- ```go
	  // Однострочный комментарий
	  
	  /*
	    Блочный
	    комментарий
	  */
	  ```
- Импорт
	- ```go
	  // Импорт одного модуля
	  import "fmt"
	  
	  // Импорт нескольких модулей
	  import (
	    "os"
	    "fmt"
	  )
	  
	  // Импорт rand по пути math
	  import (
	    "fmt"
	    "math/rand"
	  )
	  ```
- Пример минимальной программы
	- ```go
	  // Сообщаем Go о том, что этот файл относится к пакету main
	  package main
	  
	  // Модуль, с основными методами
	  import "fmt"
	  
	  // Обязательная функция
	  func main() {
	    fmt.Println("Hello, Go!") // Вывод чего-то в терминал
	    // >>Hello, Go!
	    fmt.Println("Hello,", "Go!") // Можно несколько парметров
	    // >>Hello, Go!
	  }
	  ```
-
- ```go
  package main
  
  import (
    "math"
    "strings"
  )
  
  func main() {
    math.Floor(2.75) //Округление до целого
    strings.Title("hello!") //Строка с большой буквы
  }
  ```
- ## Типы данных
	- Руны
		- Символьный код - `'A'`
	- Булевые значения
		- `true` и `false`
	- Ничего
		- ```go
		  nil
		  ```
- ## Глаголы форматирования
	- *Глагол - часть строки, которая будет заменена значением в определенном формате*
	- |Глагол|Вывод|Пример|
	  |--|--|--|
	  |`%f`|Число с плавающей точкой|`fmt.Printf("A float: %f\n", 3.1415)`|
	  |`%d`|Десятичное целое число|`fmt.Printf("An integer: %d\n", 15)`|
	  |`%s`|Строка|`fmt.Printf("A string: %s\n", "hello")`|
	  |`%t`|Логическое значение(true/false)|`fmt.Printf("A boolean: %t\n", false)`|
	  |`%v`|Произвольное значение (подходящий формат выбирается на основании типа передаваемого значения)|`fmt.Printf("Values: %v %v %v\n", 1.2, "\t", true)`|
	  |`%#v`|Произвольное значение, отформатированное в том виде, в котором оно отображается в коде Go|`fmt.Printf("Values: %#v %#v %#v\n", 1.2, "\t", true)`|
	  |`%T`|Тип передаваемого значения (int, string, ...)|`fmt.Printf("Types: %T %T %T\n", 1.2, "\t", true)`|
	  |`%%`|Знак процента(литерал)|`fmt.Printf("Percent sign: %%\n")`|
- ## Функции и методы
	- ### Стандартные функции
		- Определение типа данных
			- ```go
			  package main
			  
			  import (
			    "fmt"
			    "reflect"
			  )
			  
			  func main() {
			    fmt.Println(reflect.TypeOf(42))
			    fmt.Println(reflect.TypeOf(3.1415))
			    fmt.Println(reflect.TypeOf(true))
			    fmt.Println(reflect.TypeOf("Hello, Go!"))
			  }
			  ```
		- Дата и время
			- ```go
			  package main
			  
			  import (
			    "fmt"
			    "time"
			  )
			  
			  func main() {
			    var now time.Time = time.Now()
			    var year int = now.Year()
			    fmt.Println(year)
			  }
			  ```
		- Replace
			- ```go
			  package main
			  
			  import (
			    "fmt"
			    "strings"
			  )
			  
			  // Меняем # в строке на o
			  func main() {
			    broken := "G# r#cks!"
			    replacer := strings.NewReplacer("#", "o")
			    fixed := replacer.Replace(broken)
			    fmt.Println(fixed)
			  }
			  ```
		- Получение данных от пользователя
			- ```go
			  package main
			  
			  import (
			    "bufio"
			    "fmt"
			    "os"
			  )	
			  
			  func main() {
			    fmt.Print("Введите значение: ")
			    
			    // Создать буферизированное средство чтения текста с клавиатуры
			    reader := bufio.NewReader(os.Stdin)
			    
			    // Возвращает текст, введенный пользователем до нажатия Enter(до /n)
			    // В _(пустой идентификатор) помещается ошибка, но ничему не присваивается
			    input, _ := reader.ReadString('\n')
			    
			    fmt.Println("Введенное значение: ", input)
			  }
			  ```
		- Ошибки
			- С помощью `log`
				- ```go
				  package main
				  
				  import log
				  
				  func main() {
				    log.Fatal("Фатальная ошибка")
				  }
				  ```
			- Создание своего сообщения об ошибки с помощью `errors`
				- ```go
				  package main
				  
				  import (
				    "errors"
				    "log"
				    "fmt"
				  )
				  
				  func main() {
				    err := errors.New("Мое сообщение об ошибки")
				    fmt.Println(err.Error())
				    log.Fatal(err)
				  }
				  ```
			- Форматируем сообщение об ошибке
				- ```go
				  package main
				  
				  import (
				    "errors"
				    "log"
				    "fmt"
				  )
				  
				  func main() {
				    err := fmt.Errorf("a height of %0.2f is invalid", -2.33333)
				    fmt.Println(err.Error()) // Вариант вывода 1
				    fmt.Println(err) // Вариант вывода 2
				  }
				  ```
			- Возврат ошибки из функции
				- ```go
				  func testErrors() (int, error) {
				    return 1, nil
				  }
				  ```
		- Получить размер файла
			- ```go
			  package main
			  
			  import (
			    "fmt"
			    "log"
			    "os"
			  )
			  
			  func main() {
			    fileInfo, err := os.Stat("myFile.txt")
			    if err != nil {
			      log.Fatal("Критическая ошибка: ", err)
			    } else {
			      fmt.Println("Размер файла myFile.txt: ", string(fileInfo.Size()))
			    }
			  }
			  ```
		- Удалить лишние символы в строке
			- ```go
			  s := "\t Моя строка \n"
			  strings.TrimSpace(s)
			  ```
		- Красивый вывод `float`
			- ```go
			  fmt.printf("Вывод числа с двумя знаками после точки: %0.2f\n", 1.0/3.0)
			  
			  // Не вывод а возврат строки
			  resultString = fmt.Sprintf("Возврат числа с двумя знаками после точки: %0.2f", 1.0/3.0)
			  fmt.println(resultString)
			  ```
			- `%0.2f` является глаголом означающем количество знаков после точки
			- ![image.png](../assets/image_1733590085431_0.png)
	- При выполнении операций типы должны быть одинаковые
		- `int` умножить на `float` не получится
	- Преобразовать тип
		- `float64(varInt)`
		- `int(varFloat)`
		- Из строки в Float
		  ```go
		  import (
		    "strconv"
		    "strings"
		  )
		  
		  myStringFloat := "2.45"
		  myStringFloat = strings.TrimSpace(myStringFloat)
		  myFloat, err := strconv.ParseFloat(myStringFloat, 64) //64 количество битов
		  ```
		- Из строки в Int
		  ```go
		  import "strconv"
		  
		  myStringInt := "1000"
		  myInt, err := strconv.Atoi(myStringInt)
		  ```
	-
- ## Выражения
	- ```go
	  // Увеличить значение переменной
	  x := x + 1
	  x += 1
	  x++
	  
	  // Уменьшить значение переменной
	  y := y - 1
	  y -= 1
	  y--
	  ```
- ## Переменные
	- Объявление переменных
	  ```go
	  var varName int
	  varName = 14
	  
	  //Объявление и присвоение в одной строке
	  var varInt int = 4
	  var varInt2 = 5
	  varTest := 56
	  
	  //Несколько переменных
	  var float1, float2 float64
	  
	  //Присвоение нескольких переменных
	  float1, float2 = 1.4, 3.14
	  ```
	- Название переменных
		- Используется lowerCase
		- CamlCase используется если переменная будет экспортироваться из пакета
- ## Условные операторы
	- if -  else
		- ```go
		  if varInt < 2 {
		    fmt.Println("varInt меньше 2")
		  } else if varInt > 2 {
		    fmt.Println("varInt больше 2")
		  } else {
		    fmt.Println("varInt равен 2")
		  }
		  ```
		- Если нужно отрицание - используем `!`
		  ```go
		  if !false {
		    fmt.Println(true)
		  }
		  ```
		- И / ИЛИ
		  ```go
		  if true && true {
		    fmt.Println("Логическое И")
		  }
		  
		  if true || true {
		    fmt.Println("Логическое ИЛИ")
		  }
		  ```
- ## Циклы
	- for
		- ```go
		  for 'инициализация переменных'; 'условие'; 'изменение переменной' {
		    'тело блока цикла'
		  }
		  
		  for x := 0; x <= 6; x++ {
		    fmt.Println(x)
		  }
		  ```
		- Можно несколько параметров опустить
			- ```go
			  x := 0
			  for x <= 100 {
			    x++
			  }
			  ```
	- Остановка цикла
		- `break` - остановить выполнение цикла
		- `continue` - остановить итерацию цикла
- ## Функции
	- Пример простейшей функции
		- ```go
		  func myFuncName() {
		    fmt.Println("Тело функции")
		  }
		  ```
	- Функция с аргументами
		- ```go
		  func printSum(x int, y int) {
		    fmt.Println(x + y)
		  }
		  ```
	- Функция с возвращаемым значением
		- ```go
		  func mySum(x int, y int) int {
		    return x + y
		  }
		  ```
	- Функция, которая возвращает несколько значений
		- ```go
		  func manyReturns() (int, bool, string) {
		    return 1, true, "String"
		  }
		  ```
		- Именованные возвращаемые значения
			- ```go
			  // Функция отделяет целую часть от дробной
			  
			  func floatParts(number float64) (integerPart int, fractionalPart float64) {
			    wholeNumber := math.Floor(number)
			    return int(wholeNumber), number - wholeNumber
			  }
			  ```
- ## Указатели
	- Вывод указателя переменной
		- ```go
		  fmt.Println(&myVar)
		  ```
	- Получить тип указателя в памяти
		- ```go
		  package main
		  
		  import (
		    "fmt"
		    "reflect"
		  )
		  
		  func main() {
		    var myInt int
		    fmt.Println(reflect.TypeOf(&myInt))
		    var myFloat float64
		    fmt.Println(reflect.TypeOf(&myFloat))
		    var myBool bool
		    fmt.Println(reflect.TypeOf(&myBool))
		  }
		  ```
	- Сохранить указатель в переменную
		- ```go
		  var myInt int
		  var myIntPointer *int
		  myIntPointer = &myInt
		  fmt.Println(myIntPointer)
		  ```
	- Чтение значения по указателю
		- ```go
		  myInt := 4
		  myIntPointer := &myInt
		  fmt.Println(*myIntPointer)
		  ```
	- Запись значения по указателю
		- ```go
		  myInt := 4
		  myIntPointer := &myInt
		  *myIntpointer = 8
		  fmt.Println(myInt) // << 8
		  ```
	- Возвращение указателя функцией
		- ```go
		  func careatePointer() *float64 {
		    var myFloat = 98.5
		    return &myFloat
		  }
		  
		  func main {
		    var myFloatPointer *float64 = createPointer()
		    fmt.Println(*myPointer)
		  }
		  ```
	- Возвращение значения по указателю
		- ```go
		  func getValueInPointer(myPointer *bool) bool {
		    return *myPointer
		  }
		  
		  func main() {
		    myBoolVar := true
		    fmt.Println(getValueInPointer(&myBoolVar))
		  }
		  ```
- # Пакеты
	- *Хранение кода в отдельный файлах*
	- `Рабочая область` - директория, в которой лежит код пакетов
	- По умолчанию `рабочая область` находится в `~/go`
	- Иногда она создана в `/usr/local/go`
	- Структура каталога `go`
		- go [[$green]]==*// Каталог рабочей области*==
			- bin [[$green]]==*// Исполняемые программы*==
			- pkg [[$green]]==*// Откомпилированный код пакетов*==
			- src [[$green]]==*// Исходный код*==
				- doodad [[$green]]==*// Код пакета `doodad`*==
				- gizmo [[$green]]==*// Код пакета `gizmo`*==
					- gizmo.go
					- plug.go
	- Пример создания пакета `greeting`
		- Создаем директорию с файлом `~/go/src/greeting.go`
		- Добавляем код
			- ```go
			  // Указываем имя пакета
			  package greeting
			  
			  // Нужные импорты
			  import "fmt"
			  
			  /*
			  	Функции пакета начиаются с большой буквы 
			  	так как будут импортированы
			  */
			  func Hello() {
			    fmt.Println("Hello!")
			  }
			  
			  func Hi() {
			    fmt.Println("Hi!")
			  }
			  ```
		-