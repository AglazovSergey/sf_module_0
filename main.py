def score_game(game_core):
    '''Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число'''
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1,101, size=(1000))
    for number in random_array:
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return(score)

def game_core_v2(number):
    '''Сначала устанавливаем любое random число, а потом уменьшаем или увеличиваем его в зависимости от того, больше оно или меньше нужного.
       Функция принимает загаданное число и возвращает число попыток'''
    count = 1
    minimum = 1
    maximum = 101
    predict = np.random.randint(minimum,maximum)
    while number != predict:
        count+=1
        if number > predict: 
            minimum = predict
            predict = int((predict + maximum) / 2) # ищем среднее между диапазоном 
        elif number < predict: 
            maximum = predict
            predict = int((predict + minimum) / 2) # ищем среднее между диапазоном
    return(count) # выход из цикла, если угадали

# Проверяем
score_game(game_core_v2)