#SMOMI

При выполнении данной работы я использоавл предобученную нейронную сеть VGG16 с обученным классификатором. 

**a)** В первом пункте для аугментации данных использовал горизонтальное отражение данных с помощью 

    tf.image.random_flip_left_right(image)
    
Файл train_randomFlipping.py, lr = 1*10^(-11)
Графики:
![Image alt](https://github.com/Repsolka/SMOMI/blob/Lab4/Graphs/randomFlipping/flip_1e-11_noSmoothing.jpg)


**b)** Аугментация с помощью поворота на случайный угол [-a;a]. Файл train_rotate.py, lr = 1*10^(-11)
   
    image = tf.contrib.image.rotate(image, dgr * math.pi / 180, interpolation='BILINEAR')

Графики:
    **15 градусов**
![Image alt](https://github.com/Repsolka/SMOMI/blob/Lab4/Graphs/rotate/rot_1e-11_15.jpg)
    **30 градусов**
![Image alt](https://github.com/Repsolka/SMOMI/blob/Lab4/Graphs/rotate/rot_1e-11_30.jpg)
    **45 градусов**
![Image alt](https://github.com/Repsolka/SMOMI/blob/Lab4/Graphs/rotate/rot_1e-11_45.jpg)
    **60 градусов**
![Image alt](https://github.com/Repsolka/SMOMI/blob/Lab4/Graphs/rotate/rot_1e-11_60.jpg)
    **Сравнение**
![Image alt](https://github.com/Repsolka/SMOMI/blob/Lab4/Graphs/rotate/rot_1e-11_30_45.jpg)


**c)** В данном пункте проводилась аугментация данных с помощью случайного изменения яркости и контраста 

    tf.image.random_brightness(image, 0.5, seed=None)
    tf.image.random_contrast(image, lower=0.2, upper=1.2 seed=None)
    
Файл train_randomBrightness.py, lr = 1*10^(-11).
Графики:

![Image alt](https://github.com/Repsolka/SMOMI/blob/Lab4/Graphs/randomBrightness/bright_1e-11_noSmoothing.jpg)

    tf.image.random_brightness(image, 0.4, seed=None)
    tf.image.random_contrast(image, lower=0.2, upper=1.2 seed=None)

![Image alt](https://github.com/Repsolka/SMOMI/blob/Lab4/Graphs/randomBrightness/bright_1e-11V2.jpg)


**d)** Аугментация с использованием случайного участка изображения
 
    tf.image.random_crop(image, size=[170, 130, 3], seed=None, name=None)
  
Файл train_randomCrop.py, lr = 1*10^(-11).
Графики:
    **size=[170, 130, 3]**
![Image alt](https://github.com/Repsolka/SMOMI/blob/Lab4/Graphs/randomCrop/170x130.jpg)
    **size=[112, 112, 3]**
![Image alt](https://github.com/Repsolka/SMOMI/blob/Lab4/Graphs/randomCrop/crop_1e-11_112x112.jpg)
    **Сравнение**
![Image alt](https://github.com/Repsolka/SMOMI/blob/Lab4/Graphs/randomCrop/crop_1e-11_compare.jpg)

   **e)** Методы a, b, c, d с оптимальными параметрами
   
    image = tf.image.random_crop(image, size=[112, 112, 3], seed=None, name=None)
    image = tf.image.random_flip_left_right(image)
    image = tf.image.random_brightness(image, 0.5, seed=None)
    image = tf.image.random_contrast(image, lower=0.2, upper=1.2, seed=None)
    degree = 45
    dgr = random.uniform(-degree, degree)
    image = tf.contrib.image.rotate(image, dgr * math.pi / 180, interpolation='BILINEAR')
   
   Файл train_allAugment.py, lr = 1*10^(-11)
  Графики:
  ![Image alt](https://github.com/Repsolka/SMOMI/blob/Lab4/Graphs/AllAugment/all_1e-11_all.jpg)
  


