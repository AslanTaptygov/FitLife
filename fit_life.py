# КОНСТАНТЫ:
MILLILITERS_RECOMENDATION = 30  # рекомендуемое количество мл воды на кг
MILLILITERS_PER_LITER = 1000  # количество мл в л

# КОД:
while True:
    try:
        print('Здравствуйте! Я фитнес-бот - Ваш помощник!')

        # Ввод имени пользователя:
        user_name = input('Как мне к Вам обращаться? ')
        user_name = user_name.title()
        # Ввод возраста пользователя:
        user_age = int(input('Сколько Вам лет? '))

        print(f'Очень приятно с Вами познакомиться, {user_name}!')

        # Ввод веса пользователя:
        user_weight = float(input('Сколько Вы весите в кг? (например, 63.5) '))
        # Ввод роста пользователя:
        user_height = float(input('Какой у Вас рост в м? (например, 1.75) '))

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
        print('-' * 56)
        print('Данные введены некорректно. Пожалуйста, попробуйте снова\n')
