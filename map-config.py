global escape
from html import escape

def playerHomeFilter(poi):
    if poi['id'] == 'Sign' or poi['id'] == 'minecraft:sign':
        if poi['Text1'] == '/marker' and poi['Text2'] == 'player-home':
            return escape('Heimat von ' + poi['Text3'])

worlds['welt-1'] = './welt-1'

renders['normalrender'] = {
    'world': 'welt-1',
    'title': 'Welt 1 (2021-11-06 19:32 Uhr)',
    'rendermode': smooth_lighting,
    'dimension': 'overworld',
    'northdirection': 'upper-left',
    'markers': [
        dict(name='Heimatorte', checked=True, filterFunction=playerHomeFilter, icon='markers/marker_player_home.png'),
    ]
}

texturepath = ''
customwebassets = './assets'
outputdir = './map'
