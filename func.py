from data import *


def fight(current_enemy0):
    enemy = enemies[current_enemy0]

    while player['hp']>0 and enemy['hp']>0:
        
        player['hp'] -= enemy['attack']
        enemy['hp'] -= player['attack']
        
        print(f'Здоровье игрока = {player["hp"]}, Враг нанёс {enemy["attack"]} урона')
        print(f'Здоровье врага = {enemy["hp"]}')

        print()
        sleep(1.5)

    
    if enemy['hp'] <= 0:
        print(f'Противник - {enemy["name"]}: {enemy["win"]}')
        current_enemy0 += 1
    else:
        print(f'Противник - {enemy["name"]}: {enemy["loss"]}')

    player['hp'] = 100
    return current_enemy0





#Информация об игроке
def info_player():
    print(f'Игрок - {player["name"]}')
    print(f'Величина атаки - {player["attack"]}. Шанс критического урона ({player["attack"] * 3}ед.) равен {player["luck"]}%')
    print(f'Броня поглощает {(1 - player["armor"]) * 100}% урона')
    print()
    


#Тренировка
def training(training_type):
    
    for i in range(0, 101, 20):
        print(f'Тренировка завершена на {i}%')
        sleep(1.5)

    if training_type == '1':
        player['attack'] += 2
        print(f'Тренировка окончена! Теперь ваша величина атаки равна {player["attack"]}')

    elif training_type == '2':
        player['armor'] -= .09
        print(f'Тренировка окончена! Теперь броня поглощает {100 - player["armor"] * 100}% урона')
    print()


#Заработок денег
def earn():
    print('Добро пожаловать на завод! У тебя есть 66.66% шанс заработать 500 монет. Соответственно, 33.33% чтобы их потерять')
    result = randint(1, 100)
    sleep(1.5)
    print('Результат....')
    sleep(1.5)
    print('Страшно?!')
    if result < 67:
        print('Вы выиграли 500 монет!')
        player['money'] += 500
    else:
        print('Вы проиграли 500 монет :(')
        player['money'] -= 500
    print()
    print(f'Осталось монет: {player["money"]}')
    print()