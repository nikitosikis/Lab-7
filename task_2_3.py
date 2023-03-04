#Вариант 5

#Импорт библиотек
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

#Задание списков для данных
time = []
dros_pos = []
air_waste = []
#Извлечение данных из файла
with open('data1.csv', 'r') as f:
    for line in f:
        ind = line.split(sep=';')
        time.append(ind[0])
        dros_pos.append(ind[3])
        air_waste.append(ind[15])
    f.close()

#Перенос названий из массивов данных
time_name = time[0]
time.pop(0)
time = np.array(time, float)
dros_pos_name = dros_pos[0]
dros_pos.pop(0)
dros_pos = np.array(dros_pos, float)
air_waste_name = air_waste[0]
air_waste.pop(0)
air_waste = np.array(air_waste, float)

#Проверка корректности данных
#for i in range(len(time)):
    #print(time[i], dros_pos[i], air_waste[i])
#print(time_name,dros_pos_name,air_waste_name)

#Построение графиков от времени
plt.title('Поворот дросселя и расход воздуха в течении времени')
plt.xlabel(time_name)
plt.ylabel(dros_pos_name +' и '+ air_waste_name)
plt.plot(np.array(time), np.array(dros_pos))
plt.plot(np.array(time), np.array(air_waste))
plt.show()
#Построение графика корелляции
plt.title('График корреляции')
plt.xlabel(dros_pos_name)
plt.ylabel(air_waste_name)
plt.plot(dros_pos,air_waste,'o')
plt.show()
