



        # Перше завдання
            # б) цілими додатними та від‘ємними числами, які лежать в
            # діапазоні від – 10 до 10 включно;
            # 11. Задано список (б). Написати програму визначення
            # суми модулів елементів, розміщених після першого нульового.
print("Перша задача")
import random
import math
import array
my_list = [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
random.shuffle(my_list)
print(my_list)
y = 0
z = 0
w = 0
for i  in range(0,21):
    if z>=1:
        w=y
        ads=math.fabs(my_list[i])
        y=y+ads
        print(int(w),"+",int(ads),"=",int(y))
    if my_list[i] == 0:
        z=z+1



        # Друге Завдання
        # а) дійсними числами, які лежать в діапазоні від 0 до 1;
        # 11. Задано список (а). Написати програму, яка визначить
        # суму елементів кожного стовпчика (результат записати в інший
        # список).
print("\nДруга задача")
my_list2 =[[0.1, 0.2, 0.3,],
           [0.6, 0.7, 0.8,],
           [0,0,0]]
my_list2[2][0] = my_list2[0][0] + my_list2[1][0]
my_list2[2][1] = my_list2[0][1] + my_list2[1][1]
my_list2[2][2] = my_list2[0][2] + my_list2[1][2]

print(my_list2[0][0],my_list2[0][1],my_list2[0][2],)
print(my_list2[1][0],my_list2[1][1],my_list2[1][2],)
print(my_list2[2][0],my_list2[2][1],my_list2[2][2],)
