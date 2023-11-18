# ДЗ по основам Python решите в файле main.py

## Задача 1

Числа следует выводить через пробел. Все числа целые, по модулю не больше 1.000.000
Вводится массив, состоящий из целых чисел. Найти наибольшее среди них.

**Входные данные**  
Сначала задано число N
— количество элементов в массиве (1≤N≤100
). Далее через пробел записаны N
чисел — элементы массива. Массив состоит из целых чисел.

**Выходные данные**  
Необходимо вывести значение наибольшего элемента в массиве.
входные данные

**Пример**

входные данные
```
3
1 2 3
```
выходные данные
```
3
```

## Задача 2

Напишите программу, которая будет выполнять последовательность запросов вида ADD num, PRESENT num и COUNT (без параметра). Программу обязательно следует писать с использованием шаблонного типа set.

Выполнение каждого запроса вида ADD num должно добавлять элемент num во множество (если такой элемент уже есть, добавление ещё одной копии не изменяет множество), на экран при этом ничего не выводится.

При выполнении каждого запроса вида PRESENT num должно выдаваться сообщение «YES» или «NO» (большими буквами, в отдельной строке), соответственно тому, есть ли такой элемент во множестве; значение множества при этом не изменяется.

При выполнении каждого запроса вида COUNT должна выдаваться на экран в отдельной строке текущее количество различных элементов в множестве; значение множества при этом не изменяется.

**Входные данные**  
В первой строке стандартного входного потока задано количество запросов N (1 < N < 100000), далее следуют N строк, каждая из которых содержит по одному запросу согласно описанного формата.

Значения чисел не превышают по модулю 100000000.

**Выходные данные**  
Выводите на стандартный выход (экран) в отдельных строках результаты запросов PRESENT и COUNT; на запросы ADD ничего выводить не надо.

**Пример**  
входные данные
```
7
ADD 5
ADD 7
COUNT
PRESENT 3
PRESENT 5
ADD 3
COUNT
```
выходные данные
```
2
NO
YES
3
0
```

## Задача 3

В олимпиаде участвовало N
человек, каждый из которых мог набрать от 0 до 100 баллов. По положению об олимпиаде жюри может наградить не более 45% от числа участников, округляя их число до целого при необходимости вниз.

При этом если последний участник, попавший в 45% набирает столько же баллов, сколько первый участник, не попавший в 45%, то решение по этим участникам, и всем участникам, набравшим такой балл принимается следующим образом:

Все данные участники объявляются призерами, если набранный ими балл больше половины от максимально возможного балла.

Все эти участники не объявляются призерами, если набранный ими балл не больше половины от максимально возможного.

**Входные данные**  
Программа получает на вход информацию об участниках олимпиады (один участник - в одной строке). Строка содержит имя участника (текстовая строка с произвольным числом пробелов) и набранный данным участником балл через пробел.

**Выходные данные**  
Программа должна вывести минимальный балл, который получил участник олимпиады, ставший ее призером.

**Пример**  
входные данные
```
6
Иванов Сергей 13 80
Сергеев Петр 26 70
Сергеев Андрей 35 80
Петров Василий 13 80
Иванов Роман 35 70
Иванов Иван 26 70
```
выходные данные
```
13 35
```

# ДЗ по углубленному Python решите в файле parser.py

## Парсинг сайта с использованием Selenium.

На примере из прошлой лекции вам необходимо спарсить ***1-ую страницу сайта OZON*** и в отдельный файл сохранить следующие данные о товарах, ***цена которых выше 200 рублей***:
 
````
    🔵 Название товара

    🔵 Ссылку на товар

    🔵 Цену товара (выше 200 рублей)
````
Если цена товара не превосходит 200 рублей, то информацию об этом товаре **не** включать в файл.

Формат файла: .json либо .txt (.json будет особым преимуществом при проверке дз)
