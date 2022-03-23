import json
import requests
from icecream import ic
import pandas as pd

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
    for theme in themes:
        total_sets += theme['setCount']
        theme_names.append(theme['theme'])

    return theme_names


def get_sets_by_theme(theme_name):

    method = 'getSets'
    params = json.dumps({'theme': theme_name})
    URL = f'https://brickset.com/api/v3.asmx/{method}?apiKey={API_KEY}&userHash={USER_HASH}&params={params}'
    r = requests.get(URL)
    ic(len(r.json()['sets']))
    return r.json()['sets']


def load_sets():
    with open('sets.json') as f:
        return json.load(f)

# first 80 done


def get_all_sets():
    sets = load_sets()

    theme_names = get_theme_names()
    for theme_name in theme_names[80:100]:
        ic(theme_name)
        sets.append(get_sets_by_theme(theme_name))

    with open('sets.json', 'w') as f:
        f.write(json.dumps(sets))

    return sets


# get_all_sets()

# print(get_theme_names()[60:80])

def create_df():
    sets = []

    sets_by_theme = load_sets()[:10]
    for theme in sets_by_theme:
        for set_ in theme:
            sets.append(set_)

    df = pd.DataFrame(sets)
    df['licensed'] = df['name'].apply(lambda x: x in LICENSED)

    print(df.head())


create_df()
