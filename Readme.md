#Тестирование калькулятора


##Требования
В связи с тем, что четкие требовани отсутствуют, то для тестирования пердлагаю руководствоваться
документацией в сваггере.  
Согласно модели body, описанной для метода API POST /test/calculate, левый и правый
операнды на вход принимают значения типа Integer, исходя из этого, предположим, что результат
тоже быть только типа Integer.
Соответственно в качестве операндов будут подаваться значения:
1. Внутри диапазона от −2147483648 до +2147483647;
2. Граничные значения диапазона −2147483648 до +2147483647;
3. Вне дипазона −2147483648 до +2147483647.


#Запуск тестов

