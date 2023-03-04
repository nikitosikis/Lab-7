#Вариант 5

#Импорт библиотек
import time
import numpy as np
import random

#task 1

#обычный список с миллионом элементов через генератор списков
casual_array = [random.randint(1, 10) for i in range(1 * 10**6)]
# numpy array созданный из массива такой же размерности
numpy_array = np.array([random.randint(1, 10) for i in range(1 * 10**6)])

#Запуск таймера
time.perf_counter()

#Перемножение питоновского массива
casual_mlt = 1
for i in casual_array:
    casual_mlt *= i
casual_time = time.perf_counter()
casual_type = type(casual_mlt)

#Перемножение массива numpy
numpy_mlt = np.prod(numpy_array)
numpy_time = time.perf_counter() - casual_time
#Я не понял, зачем в методичке указана функция numpy.multiply(), если на вход она принимает 2 значения, а у нас всего один массив, поэтому я использовал функцию numpy.prod(), которая перемножает входной список
numpy_type = type(np.prod(numpy_array))

# Как мы видим numpy делает вычисления быстрее в несоотносимым с классическими методами питона отношении(возможно это потому, что numpy написан на C++
print(casual_time, casual_type, numpy_time, numpy_type)