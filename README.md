#SMOMI
В задаче используется полносвязная сеть из пяти слоёв: один Flatten, четыре Dense.
Слои Dense имеют 128, 64, 64, 10 нейронов соответственно. Первые три слоя Dense используют активацию relu, в последнем же используется активация softmax.

При обучении используется функция потерь SparseCategoricalCrossentropy, оптимизатор adam, метрика точности accuracy. Цикл обучения состоит из 30 эпох.

Итоговая точность на обучающей выборке 0.4282
Итоговая точность на тестовых данных 0.4175

Графики метрики точности
![Image alt](https://github.com/Repsolka/SMOMI/blob/Lab1/epoch_acc.jpg)
![Image alt](https://github.com/Repsolka/SMOMI/blob/Lab1/epoch_val_acc.jpg)

Графики функции потерь
![Image alt](https://github.com/Repsolka/SMOMI/blob/Lab1/epoch_loss.jpg)
![Image alt](https://github.com/Repsolka/SMOMI/blob/Lab1/epoch_val_loss.jpg)


