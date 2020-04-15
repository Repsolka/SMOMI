#SMOMI

При выполнении данной работы я использоавл предобученную нейронную сеть VGG16 с обученным классификатором. 

**a)** В первом пункте для аугментации данных использовал горизонтальное отражение данных с помощью 

    tf.image.random_flip_left_right(image)
Файл train_randomFlipping.py, lr = 1*10^(-11)
Графики:

![Image alt](https://github.com/Repsolka/SMOMI/blob/Lab4/randomFlipping/flip_1e-11.jpg)

**б)** Аугментация с помощью поворота на случайный угол [-a;a]. Файл train_rotate.py, lr = 1*10^(-11)
   
    image = tf.contrib.image.rotate(image, dgr * math.pi / 180, interpolation='BILINEAR')

Графики:
30 градусов
![Image alt](https://github.com/Repsolka/SMOMI/blob/Lab4/Graphs/rotate/rot_1e-11_30d.jpg)
45 градусов
![Image alt](https://github.com/Repsolka/SMOMI/blob/Lab4/Graphs/rotate/rot_1e-11_45d.jpg)
Вместе
![Image alt](https://github.com/Repsolka/SMOMI/blob/Lab4/Graphs/rotate/rot_1e-11_30_45.jpg)


**c)** В данном пункте проводилась аугментация данных с помощью случайного изменения яркости и контраста 

    tf.image.random_brightness(image, 0.5, seed=None)
    tf.image.random_contrast(image, lower=0.2, upper=1.2 seed=None)
Файл train_randomBrightness.py, lr = 1*10^(-11).
Графики:

![Image alt](https://github.com/Repsolka/SMOMI/blob/Lab4/Graphs/randomBrightness/bright_1e-11.jpg)

    tf.image.random_brightness(image, 0.4, seed=None)
    tf.image.random_contrast(image, lower=0.2, upper=1.2 seed=None)
lr = 1*10^(-11).
Графики:

![Image alt](https://github.com/Repsolka/SMOMI/blob/Lab4/Graphs/randomBrightness/bright_1e-11V2.jpg)


