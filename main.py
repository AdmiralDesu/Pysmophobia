from models_pydantic import Game, Ghost, Player
import openpyxl
from datetime import time
import os
import psycopg2
import json


connection_data = os.environ['connection_data']
connection = psycopg2.connect(connection_data)
cursor = connection.cursor()

mimic = Ghost(**{
    'name': 'Mimic',
    'evidences': {
        'evidence_1': 'Spirit Box',
        'evidence_2': 'Fingerprints',
        'evidence_3': 'Freezing Temperatures'
    },
    'strength': 'Can mimic the actions of other ghosts',
    'weakness': 'Induces Ghost Orbs as fourth evidence',

})

cursor.execute('''
select * from "Pysmophobia_data".ghost
''')
result = cursor.fetchall()

print(f'{result=}')

duration_of_game = time(hour=0, minute=30, second=20)
print(duration_of_game)
print(type(duration_of_game))

player_admiral = Player(**{
    'name': 'admiral'
})

player_g = Player(**{
    'name': 'g'
})

player_u = Player(**{
    'name': 'u'
})

player_s = Player(**{
    'name': 's'
})

player_n = Player(**{
    'name': 'n'
})

game_1 = Game(**{
    'duration': duration_of_game,
    'ghost_id': 1,
    'difficulty': 'Кошмар',
    'evidences': ['Улика 1'],
    'players': [player_s.name, player_g.name, player_u.name, player_admiral.name],
    'right_or_not': ['1'],
    'dead_or_not': ['0'],
    'game_version': '0.5.1.0',
    'cursed_possession': 'Tarot Cards'
})

print(game_1)
print(game_1.players)
print(game_1.duration)







