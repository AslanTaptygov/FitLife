MILLILITERS_RECOMENDATION = 30
MILLILITERS_PER_LITER = 1000
DIVING_LINE = 56


def program():
    """
    Бот для высчитывания ИМТ и нормы воды
    >>>Запрашивает:
    1) Имя пользователя (user_name)
    2) Возраст пользователя (user_age)
    3) Вес пользователя (user_weight)
    4) Рост пользователя (user_height)
    >>>Возвращает: ИМТ и норму потребления воды
    >>>КОНСТАНТЫ:
    1) MILLILITERS_RECOMENDATION - рекомендованное количество мл на кг веса
    2) MILLILITERS_PER_LITER - количество мл в л
    3) DIVING_LINE - нужна для создания разделительной черты
       (если программа завершила работу с ошибкой)
    """
    while True:
        try:
            print('Здравствуйте! Я фитнес-бот - Ваш помощник!')

            user_name = input('Как мне к Вам обращаться? ')
            user_name = user_name.title()
            user_age = int(input('Сколько Вам лет? '))

            print(f'Очень приятно с Вами познакомиться, {user_name}!')

            user_weight = input('Сколько Вы весите в кг? ')
            user_weight = float(user_weight.replace(',', '.'))

            user_height = input('Какой у Вас рост в м? ')
            user_height = float(user_height.replace(',', '.'))

            # Рассчёт индекса массы тела (ИМТ):
            bmi = round(user_weight / (user_height ** 2), 1)

            # Рассчёт нормы воды (сначала в мл, потом в л):
            water_ml = user_weight * MILLILITERS_RECOMENDATION
            water_l = water_ml / MILLILITERS_PER_LITER

            print(f'\nОтчёт для пользователя: {user_name} ({user_age} г.)')
            print(f'Ваш индекс массы тела (ИМТ): {bmi}')
            print(f'Рекомендуемая норма воды: {water_l:.1f} л в день')
            print('\nРасчёт окончен. Будьте здоровы!')
            break
        except ValueError:
            print('-' * DIVING_LINE)
            print('Данные введены некорректно. Пожалуйста, попробуйте снова\n')


program()
