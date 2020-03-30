#SMOMI

 В задаче используется свёрточная сеть. В процессе выполнения задания изменялось количество слоёв Conv2D и MaxPool2D, а так же количество свёрток в слоях Conv2D и скорость обeчения lr (BATCH_SIZE = 1 NUM_CLASSES = 2). 
 Были исследованы следующие конфигурации сети:

1. Свёрточная нейронная сеть с двумя слоями Conv2D(filters=8, kernel_size=3), lr = 1*10^(-9), epoch=200

График метрики точности
![Image alt](https://github.com/Repsolka/SMOMI/blob/Lab2/acc_1*10%5E(-9)%20_stock.jpg)

График функции потерь 
![Image alt](https://github.com/Repsolka/SMOMI/blob/Lab2/loss_1*10%5E(-9)_stock.jpg)


2. Свёрточная нейронная сеть с тремя слоями Conv2D(filters=8, kernel_size=3), lr = 1*10^(-9), epoch=200

График метрики точности
![Image alt](https://github.com/Repsolka/SMOMI/blob/Lab2/acc_1*10%5E(-9)_1Conv83.jpg)

График функции потерь 
![Image alt](https://github.com/Repsolka/SMOMI/blob/Lab2/loss_1*10%5E(-9)_1Conv83.jpg)

3. Свёрточная нейронная сеть с двумя слоями Conv2D(filters=8, kernel_size=3), lr = 2*10^(-9), epoch=200

График метрики точности
![Image alt](https://github.com/Repsolka/SMOMI/blob/Lab2/acc_2*10%5E(-9)_stock.jpg)

График функции потерь 
![Image alt](https://github.com/Repsolka/SMOMI/blob/Lab2/loss_2*10%5E(-9)_stock.jpg)

4. Свёрточная нейронная сеть с тремя слоями Conv2D(filters=8, kernel_size=3), lr = 2*10^(-9), epoch=87

График метрики точности
![Image alt](https://github.com/Repsolka/SMOMI/blob/Lab2/acc_2*10%5E(-9)_1Conv83.jpg)

График функции потерь 
![Image alt](https://github.com/Repsolka/SMOMI/blob/Lab2/loss_2*10%5E(-9)_1Conv83.jpg)

5. Свёрточная нейронная сеть с одним слоем Conv2D(filters=16, kernel_size=3) и думя слоями Conv2D(filters=8, kernel_size=3), lr = 2*10^(-9), epoch=87

График метрики точности
![Image alt](https://github.com/Repsolka/SMOMI/blob/Lab2/loss_2*10%5E(-9)_1Conv163.jpg)

График функции потерь 
![Image alt](https://github.com/Repsolka/SMOMI/blob/Lab2/loss_2*10%5E(-9)_1Conv163.jpg)

6. Свёрточная нейронная сеть с одним слоем Conv2D(filters=16, kernel_size=3) и тремя слоями Conv2D(filters=8, kernel_size=3), lr = 2*10^(-9), epoch=87

График метрики точности
![Image alt](https://github.com/Repsolka/SMOMI/blob/Lab2/acc_2*10%5E(-9)_2Conv816.jpg)

График функции потерь 
![Image alt](https://github.com/Repsolka/SMOMI/blob/Lab2/loss_2*10%5E(-9)_2Conv816.jpg)


7. Свёрточная нейронная сеть с одним слоем Conv2D(filters=32, kernel_size=3),одним слоем Conv2D(filters=16, kernel_size=3) и двумя слоями Conv2D(filters=8, kernel_size=3), lr = 2*10^(-9), epoch=87

График метрики точности
![Image alt](https://github.com/Repsolka/SMOMI/blob/Lab2/acc_2*10%5E(-9)_2Conv1632.jpg)

График функции потерь 
![Image alt](https://github.com/Repsolka/SMOMI/blob/Lab2/loss_2*10%5E(-9)_2Conv1632.jpg)

8. Свёрточная нейронная сеть с одним слоем Conv2D(filters=32, kernel_size=3) и одним слоем Conv2D(filters=16, kernel_size=3), lr = 2*10^(-9), epoch=87

График метрики точности
![Image alt](https://github.com/Repsolka/SMOMI/blob/Lab2/acc_2*10%5E(-9)_Conv3216.jpg)

График функции потерь 
![Image alt](https://github.com/Repsolka/SMOMI/blob/Lab2/loss_2*10%5E(-9)_2Conv3216.jpg)
