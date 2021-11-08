global escape
from html import escape

def playerHomeFilter(poi):
    if poi['id'] == 'Sign' or poi['id'] == 'minecraft:sign':
        if poi['Text1'] == '/marker' and poi['Text2'] == 'player-home':
            return escape('Heimat von %s %s' % (poi['Text3'], poi['Text4']))

def castleFilter(poi):
    if poi['id'] == 'Sign' or poi['id'] == 'minecraft:sign':
        if poi['Text1'] == '/marker' and poi['Text2'] == 'castle':
            return escape('%s %s' % (poi['Text3'], poi['Text4']))

def playerIconsFilter(poi):
    if poi['id'] == 'Player':
        poi['icon'] = 'https://overviewer.org/avatar/%s' % poi['EntityId']
        return 'Letzte bekannte Position von %s' % poi['EntityId']

worlds['welt-1'] = './welt-1'

renders['normalrender'] = {
    'world': 'welt-1',
    'title': 'Welt 1 (2021-11-08 20:55 Uhr)',
    'rendermode': smooth_lighting,
    'dimension': 'overworld',
    'northdirection': 'upper-left',
    'showspawn': True,
    'markers': [
        dict(name='Heimatorte', checked=True, filterFunction=playerHomeFilter, icon='markers/marker_player_home.png'),
        dict(name='Burgen', checked=True, filterFunction=castleFilter, icon='markers/marker_tower.png'),
        dict(name='Spieler', checked=False, filterFunction=playerIconsFilter)
    ]
}

texturepath = ''
customwebassets = './assets'
outputdir = './map'
