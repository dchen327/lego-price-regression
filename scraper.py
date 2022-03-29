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
    ignore = ['Books', 'Collectable Minifigures',
              'Duplo', 'Gear', 'Service Packs']
    with open('themes.json') as f:
        themes = json.load(f)['themes']

    theme_names = []
    total_sets = 0
    for theme in themes:
        theme_name = theme['theme']
        if theme_name not in ignore and theme['setCount'] > 30:
            total_sets += theme['setCount']
            if theme['setCount'] >= 300:
                ic(theme_name, theme['setCount'])
            theme_names.append(theme_name)

    # ic(total_sets)

    return theme_names


get_theme_names()


def get_sets_by_theme(theme_name):

    method = 'getSets'
    params = json.dumps({'theme': theme_name, 'pageSize': 500})
    URL = f'https://brickset.com/api/v3.asmx/{method}?apiKey={API_KEY}&userHash={USER_HASH}&params={params}'
    r = requests.get(URL)
    return r.json()['sets']


def load_sets():
    with open('all_sets.json') as f:
        return json.load(f)


# count num of sets
# c = 0
# sets = load_sets()
# for theme in sets:
#     set_ct = 0
#     for set_ in theme:
#         set_ct += 1
#     ic(set_ct)
#     c += set_ct

# ic(c)


# def get_all_sets():
#     sets = []

#     theme_names = get_theme_names()
#     for theme_name in theme_names:
#         ic(theme_name)
#         sets.append(get_sets_by_theme(theme_name))

#     with open('sets.json', 'w') as f:
#         f.write(json.dumps(sets))

#     return sets


def grab_missing_data():
    gt_500 = ['City', 'Promotional', 'Star Wars', 'Town']


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
