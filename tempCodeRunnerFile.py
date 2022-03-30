tSets'
params = json.dumps({'theme': 'Star Wars', 'pageSize': 500, 'pageNumber': 2})
URL = f'https://brickset.com/api/v3.asmx/{method}?apiKey={API_KEY}&userHash={USER_HASH}&params={params}'
r = requests.get(URL)
sets_ = r.json()['sets']

ic(len(sets_))