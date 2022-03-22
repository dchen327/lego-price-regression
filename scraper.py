import json
import requests
from icecream import ic

# pulled from set categories
LICENSED = ['Avatar The Last Airbender', 'Batman', 'Brick Sketches', 'BrickHeadz', 'Cars', 'DC Comics Super Heroes', 'DC Super Hero Girls', 'Disney', 'Galidor', 'Ghostbusters', 'Harry Potter', 'Horizon', 'Indiana Jones', 'Jurassic World', 'Marvel Super Heroes', 'Minecraft', 'Minions: The Rise of Gru', 'Mixels', 'Overwatch', 'Pirates of the Caribbean', 'Prince of Persia', 'Scooby-Doo',
            'Speed Champions', 'Spider-Man', 'SpongeBob SquarePants', 'Star Wars', 'Stranger Things', 'Super Mario', 'Teenage Mutant Ninja Turtles', 'The Angry Birds Movie', 'The Hobbit', 'The LEGO Batman Movie', 'The LEGO Movie', 'The LEGO Movie 2', 'The LEGO Ninjago Movie', 'The Lone Ranger', 'The Lord of the Rings', 'The Powerpuff Girls', 'The Simpsons', 'Toy Story', 'Trolls World Tour', 'Unikitty', 'Vidiyo']


API_KEY = '3-7NSU-8Pqh-eDwah'
USER_HASH = 'krrngmEXdD'




def get_theme_names():
    with open('themes.json') as f:
    themes = json.load(f)['themes']

    theme_names = []
    total_sets = 0
    c = 0
    for theme in themes:
        total_sets += theme['setCount']
        theme_names.append(theme['theme'])
        c += 1
    
    return theme_names


def get_sets_by_theme(theme_name):

    method = 'getSets'
    params = json.dumps({'theme': 'theme_name'})
    URL = f'https://brickset.com/api/v3.asmx/{method}?apiKey={API_KEY}&userHash={USER_HASH}&params={params}'
    r = requests.get(URL)
    print(r.json())
    return r.json()['sets']


def get_all_sets():
    sets = []
    for theme_name in theme_names:
        ic(theme_name)
        sets.append(get_sets_by_theme(theme_name))
        break

    with open('sets.json', 'w') as f:
        f.write(json.dumps(sets))

    return sets


get_all_sets()
