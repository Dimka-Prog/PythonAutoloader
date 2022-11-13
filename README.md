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
