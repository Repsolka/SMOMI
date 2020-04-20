#SMOMI

**Лабораторная работа 5**

**Задание 1**

**а)** Пошаговое затухание, файл train_StepDecay_1.py. 
       
    def step_decay(epoch):
        initial_lrate = 0.0000000001
        drop = 0.5
        epochs_drop = 10.0
        lrate = initial_lrate * math.pow(drop, math.floor((1+epoch)/epochs_drop))
        return lrate
![Image alt] (https://github.com/Repsolka/SMOMI/blob/Lab5/Graphs/StepDecay.jpg) 

**б)** Экспоненциальное затухание, файл train_expDecay_1.py. 
       
    def exp_decay(epoch):
       initial_lrate = 0.0000000001
        k = 0.1
        lrate = initial_lrate * np.exp(-k*epoch)
        return lrate
![Image alt] (https://github.com/Repsolka/SMOMI/blob/Lab5/Graphs/ExpDecay.jpg) 

**Задание 2**

**а)** "Предварительный разогрев" с последующим пошаговым затуханием, файл train_StepDecay_warmUp.py. 

    def step_decay(epoch):
        initial_lrate = 0.0000000001
        drop = 0.5
        epochs_drop = 10.0
        start_lr = 0
        finish_lr = 0.0000000001
        length = 10
        if epoch <= length:
           return epoch * (finish_lr - start_lr)/(length) + start_lr
        else:
           lrate = initial_lrate * math.pow(drop, math.floor((1+epoch)/epochs_drop))
           return lrate
![Image alt] (https://github.com/Repsolka/SMOMI/blob/Lab5/Graphs/StepDecay_WarmUp.jpg) 

**б)** "Предварительный разогрев" с последующим экспоненциальным затуханием, файл train_expDecay_warmUp.py. 

    def exp_decay(epoch):
       initial_lrate = 0.0000000001
       start_lr = 0
       finish_lr = 0.0000000001
       length = 10
       k = 0.1
       if epoch <= length:
           return epoch * (finish_lr - start_lr)/(length) + start_lr
       else:
           lrate = initial_lrate * np.exp(-k*epoch)
           return lrate
![Image alt] (https://github.com/Repsolka/SMOMI/blob/Lab5/Graphs/ExpDecay_WarmUp.jpg) 

![Image alt](https://github.com/Repsolka/SMOMI/blob/Lab4/Graphs/rotate/rot_1e-11_30d.jpg)
