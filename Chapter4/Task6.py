import numpy as np
import matplotlib.pyplot as plt

kernal = np.array([0, .1, .3, .8, 1, .8, .3, .1, 0])
kernal /= kernal.sum()
values = np.random.normal(size=(1, 100))

risult = []
for i in range(kernal.size, values.size):
    risult.append(kernal @ values[0, i - kernal.size: i])

risult = np.array(risult)


fig, axe = plt.subplots(1, 3, figsize=(15, 5))


axe[0].plot(kernal, marker="*")
axe[0].set_title("Ядро")
# axe[0].axis("square")
# axe[0].axis([0, 1, -1, 1])

axe[1].plot(values[0], marker="*")
axe[1].set_title("Сигнал временного ряда")
# axe[1].axis("square")
# axe[1].axis([0, 30, -10, 10])

axe[2].plot(values[0], marker="*", label="Сигнал")
axe[2].plot(risult, marker="o", label="Обнаружение скачков", linestyle='--')
axe[2].set_title("Результ")
axe[2].legend()
# axe[2].axis("square")
# axe[2].axis([0, 30, -10, 10])

plt.show()