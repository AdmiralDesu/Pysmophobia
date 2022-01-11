from models_pydantic import Ghost
import psycopg2
import os
import json


connection = psycopg2.connect(os.environ['connection_data'])

cursor = connection.cursor()

json_ghosts = dict()

json_ghosts['Mimic'] = {
    'ghost_id': 1,
    'name': 'Mimic',
    'evidences': {
        'evidence_1': 'Spirit Box',
        'evidence_2': 'Fingerprints',
        'evidence_3': 'Freezing Temperatures'
    },
    'strength': ['Can mimic the actions of other ghosts'],
    'weakness': ['Induces Ghost Orbs as fourth evidence'],
    'ability': ['Mimic strength and weakness of other ghosts'],
    'uniqueness': ['Have Ghost Orbs as fourth (or third on Nightmare difficulty) evidence']
}

json_ghosts['Banshee'] = {
    'ghost_id': 2,
    'name': 'Banshee',
    'evidences': {
        'evidence_1': 'Fingerprints',
        'evidence_2': 'Ghost Orb',
        'evidence_3': 'D.O.T.S Projector'
    },
    'strength': ['Focuses on the same player until that player is killed or has left the game'],
    'weakness': ['Crucifixes have an effective range of 5 meters instead of 3 meters'],
    'ability': ['Focuses on the same player during hunt', 'Rare chance to hunt at any sanity percentage'],
    'uniqueness': ['Have unique sound on Parabolic Microphone']
}

json_ghosts['Demon'] = {
    'ghost_id': 3,
    'name': 'Demon',
    'evidences': {
        'evidence_1': 'Fingerprints',
        'evidence_2': 'Ghost Writing',
        'evidence_3': 'Freezing Temperatures'
    },
    'strength': ['Hunts more often than any other type of ghost'],
    'weakness': ['Reduced sanity drain from various cursed possessions'],
    'ability': ['Can hunt from 70% sanity', 'Rare chance to hunt at any sanity percentage'],
    'uniqueness': ['Chance of very early hunt', '20 seconds cooldown of hunt instead of usual 25']
}

json_ghosts['Goryo'] = {
    'ghost_id': 4,
    'name': 'Goryo',
    'evidences': {
        'evidence_1': 'EMF Level 5',
        'evidence_2': 'Fingerprints',
        'evidence_3': 'D.O.T.S Projector'
    },
    'strength': ['A Goryo will usually only show itself on camera if there are no people nearby'],
    'weakness': ['They are are rarely seen far from their place of death'],
    'ability': ['Only shows itself passing through D.O.T.S. on video camera'],
    'uniqueness': ['Always have D.O.T.S Projector as evidence on Nightmare difficulty']
}

json_ghosts['Hantu'] = {
    'ghost_id': 5,
    'name': 'Hantu',
    'evidences': {
        'evidence_1': 'Fingerprints',
        'evidence_2': 'Ghost Orb',
        'evidence_3': 'Freezing Temperatures'
    },
    'strength': ['Lower temperatures allow the Hantu to move at faster speeds.'],
    'weakness': ['Hantus move slower in warmer areas.'],
    'ability': ['Moves much quicker in colder areas during hunts', 'Emits frosty breath in freezing rooms'],
    'uniqueness': ['You can see her frosty breath while hunt']
}

json_ghosts['Jinn'] = {
    'ghost_id': 6,
    'name': 'Jinn',
    'evidences': {
        'evidence_1': 'EMF Level 5',
        'evidence_2': 'Fingerprints',
        'evidence_3': 'Freezing Temperatures'
    },
    'strength': ['A Jinn will travel at a faster speed if its victim is far away'],
    'weakness': ["Turning off the location's power source will prevent the Jinn from using its ability"],
    'ability': ['Travels at faster speeds if its target is far away'],
    'uniqueness': ['Jinn will have high speed only if he sees player',
                   'On 2m distance from player will abruptly reduce speed',
                   'Never turn off Fuse Box']
}

json_ghosts['Mare'] = {
    'ghost_id': 7,
    'name': 'Mare',
    'evidences': {
        'evidence_1': 'Spirit Box',
        'evidence_2': 'Ghost Orb',
        'evidence_3': 'Ghost Writing'
    },
    'strength': ['Can hunt at higher sanity levels (60% if lights are off)', 'Will try to turn off lights more often'],
    'weakness': ["Turning lights on will lower its hunt sanity threshold to 40%"],
    'ability': ['Turn off lights after hunt'],
    'uniqueness': ["Don't turn on lights",
                   'Try turn off lights and Fuse Box very often']
}

json_ghosts['Myling'] = {
    'ghost_id': 8,
    'name': 'Myling',
    'evidences': {
        'evidence_1': 'EMF Level 5',
        'evidence_2': 'Fingerprints',
        'evidence_3': 'Ghost Writing'
    },
    'strength': ['Has quieter footsteps during hunts'],
    'weakness': ["Produces paranormal sounds more frequently"],
    'ability': ['Turn off lights after hunt'],
    'uniqueness': ["Very quiet while hunt (no sound but footsteps)",
                   'Very noisy while not hunt (use Parabolic Microphone)']
}

json_ghosts['Obake'] = {
    'ghost_id': 9,
    'name': 'Obake',
    'evidences': {
        'evidence_1': 'EMF Level 5',
        'evidence_2': 'Fingerprints',
        'evidence_3': 'Ghost Orb'
    },
    'strength': ['When interacting with the environment, an Obake will rarely leave a trace'],
    'weakness': ["May leave behind six-fingered Fingerprints"],
    'ability': ['Can leave fingerprints that disappear quicker'],
    'uniqueness': ["On Nightmare difficulty always have Fingerprints",
                   'Can leave Fingerprints with six fingers (Mimic can do it to!)']
}

json_ghosts['Oni'] = {
    'ghost_id': 10,
    'name': 'Oni',
    'evidences': {
        'evidence_1': 'EMF Level 5',
        'evidence_2': 'Freezing Temperatures',
        'evidence_3': 'D.O.T.S Projector'
    },
    'strength': ['More active when people are nearby', 'Throws objects at great speeds'],
    'weakness': ["Easy to identify if it's more active"],
    'ability': ['Can throw items with great speed to far distances'],
    'uniqueness': ["Become more active if see group of players",
                   'Hunt will end sooner if players go to different places']
}

json_ghosts['Onryo'] = {
    'ghost_id': 11,
    'name': 'Onryo',
    'evidences': {
        'evidence_1': 'Spirit Box',
        'evidence_2': 'Ghost Orb',
        'evidence_3': 'Freezing Temperatures'
    },
    'strength': ['Extinguishing a flame can cause an Onyro to attack.'],
    'weakness': ["When threatened, this ghost will be less likely to hunt."],
    'ability': ['Can throw items with great speed to far distances'],
    'uniqueness': ["Become more active if see group of players",
                   'Hunt will end sooner if players go to different places']
}


with open('../ghosts.json', 'w') as json_file:
    json.dump(json_ghosts, json_file, indent=2)


connection.close()
