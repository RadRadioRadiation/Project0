from time import *
from random import *


player = {
    'name': '',
    'armor': 0.95,
    'hp': 100,
    'attack': 5,
    'luck': 10,
    'money': 10000,
    'inventory': []
}


enemies = [
    {
        'name' : 'Волк',
        'hp': 10,
        'attack' : 5, 
        'script' : 'Зачем ты здесь? Ты не сможешь меня победить. Принцесса моя!',
        'win' : 'Ты — достойный противник, но до принцессы тебе еще далеко.',
        'loss' : 'Ха! Я же говорил, тебе меня не победить.Уходи и не возвращайся сюда!'
    },
    {
        'name' : 'Шакал',
        'hp' : 25,
        'attack' : 20,
        'script' : 'Чего пришел? не видишь, у меня обед!',
        'win' : 'Больше не обижай невинных зверушек!',
        'loss' : 'Кого ты собрался защищать, если сам себя защитить не можешь, хаха!'
    },
    {
        'name' : 'Змея',
        'hp' : 200,
        'attack' : 30,
        'script' : 'Как ты посмел зайти на мою территорию?! Я тебе придам урок, если сию секунду не скроешся!',
        'win' : 'Ладно! так уж и быть! разрешу тебе присутсвовать на моей территории..',
        'loss' : 'А я предупреждал! Иди от сюда что б глаза мои тебя не видели!'
    }
]