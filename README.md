#SMOMI

В файле train.py была получена нейронная сеть VGG16. Данная сеть не обучалась: потери всегда уходили в nan и точность на тренировочных данных всегда варьировалась в районе 0.2571.
Примеры обучения модели VGG16:

BUTCH_SIZE=8, lr=0.0000005
![Image alt](https://github.com/Repsolka/SMOMI/blob/Lab3/Graphs/JustVGG16/butch8_0.0000005.jpg)

BUTCH_SIZE=8, lr=0.0000003
![Image alt](https://github.com/Repsolka/SMOMI/blob/Lab3/Graphs/JustVGG16/butch8_0.0000003.jpg)

BUTCH_SIZE=8, lr=0.0000001
![Image alt](https://github.com/Repsolka/SMOMI/blob/Lab3/Graphs/JustVGG16/butch8_0.0000001.jpg)

В файле train_freeze.py использована предобученная на image.net сеть VGG16. В данной сети были заморожены свёрточные слои и 
производилось обучение классификатора с последующим сохранением весовых коэффициентов.
Графики для замороженной сети:

BUTCH_SIZE=8, lr=0.000003
![Image alt](https://github.com/Repsolka/SMOMI/blob/Lab3/Graphs/PreTrainedFreeze/freeze_8_0.000003.jpg)

BUTCH_SIZE=8, lr=0.0000009
![Image alt](https://github.com/Repsolka/SMOMI/blob/Lab3/Graphs/PreTrainedFreeze/freeze_8_0.0000009.jpg)

BUTCH_SIZE=8, lr=0.000001
![Image alt](https://github.com/Repsolka/SMOMI/blob/Lab3/Graphs/PreTrainedFreeze/freeze_8_0.000001.jpg)

Сравнение графиков с темпами обучения 0.0000009(оранжевый) и 0.000001(синий)
![Image alt](https://github.com/Repsolka/SMOMI/blob/Lab3/Graphs/PreTrainedFreeze/freeze_8_1vs09.jpg)


В файле train_defrost.py использована предобученная на image.net сеть VGG16. В данной сети были разморожены свёрточные слои
и использованны весовые коэффициенты из предыдущего запуска. 
Графики для размороженной сети:

BUTCH_SIZE=8, lr=0.00000000001
![Image alt](https://github.com/Repsolka/SMOMI/blob/Lab3/Graphs/PreTrainedDefrost/defrost_8_0.00000000001.jpg)




