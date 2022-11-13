## Установка
## Применение
Ипортируем библиотеку `from autoloader import loader` <br/>
Оборачиваем вызов функции в try except <br/>
``try: 
    //Function call 
except ValueError as error: 
    print('Error: ' + str(error))``
