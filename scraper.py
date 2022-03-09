import json
import requests

# pulled from set categories
LICENSED = ['Avatar The Last Airbender', 'Batman', 'Brick Sketches', 'BrickHeadz', 'Cars', 'DC Comics Super Heroes', 'DC Super Hero Girls', 'Disney', 'Galidor', 'Ghostbusters', 'Harry Potter', 'Horizon', 'Indiana Jones', 'Jurassic World', 'Marvel Super Heroes', 'Minecraft', 'Minions: The Rise of Gru', 'Mixels', 'Overwatch', 'Pirates of the Caribbean', 'Prince of Persia', 'Scooby-Doo',
            'Speed Champions', 'Spider-Man', 'SpongeBob SquarePants', 'Star Wars', 'Stranger Things', 'Super Mario', 'Teenage Mutant Ninja Turtles', 'The Angry Birds Movie', 'The Hobbit', 'The LEGO Batman Movie', 'The LEGO Movie', 'The LEGO Movie 2', 'The LEGO Ninjago Movie', 'The Lone Ranger', 'The Lord of the Rings', 'The Powerpuff Girls', 'The Simpsons', 'Toy Story', 'Trolls World Tour', 'Unikitty', 'Vidiyo']


# API_KEY = '3-7NSU-8Pqh-eDwah'
# method = 'getThemes'
# URL = f'https://brickset.com/api/v3.asmx/{method}?apiKey={API_KEY}'

# r = requests.get(URL)
# with open('themes.json', 'w') as f:
#     json.dump(r.json(), f)
# themes = r.json()['themes']

with open('themes.json') as f:
    themes = json.load(f)['themes']

c = 0
for theme in themes:
    if theme['setCount'] > 20 and theme['yearTo'] > 2020:
        c += 1
        print(theme['theme'])
print(c)
