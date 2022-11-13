## Установка
## Применение
Ипортируем библиотеку `from autoloader import loader`\n
Оборачиваем вызов функции в try except
`try:
	//Function call
except ValueError as error:
    print('Error: ' + str(error))`
