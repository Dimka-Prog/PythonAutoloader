## Установка
## Применение
1. Ипортируем библиотеку: `from autoloader import loader`
2. Оборачиваем вызов функции `loader()` в try except <br/>
```py 
try: 
    #Function call 
except ValueError as error: 
    print('Error: ' + str(error))
```
<pre>
Функция `loader(projectFolder, file)` принимает два аргумента:<br/>
    `projectFolder` - название папки проекта <br/>
    `file` - файл, до которого нужно получить путь <br/>

В результате работы, данная функция возвращает абсолютный путь до файла в формате строки. Если файл не был найден, то выдаст исключение, которое выведет сообщение об ошибке.
</pre>

    
    
