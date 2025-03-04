global escape
from html import escape

SHRINE_SERVICES = {
    't': 'Teleportation'
}

def playerHomeFilter(poi):
    if poi['id'] == 'Sign' or poi['id'] == 'minecraft:sign':
        if poi['Text1'] == '/marker' and poi['Text2'] == 'player-home':
            return escape('Heimat von %s %s' % (poi['Text3'], poi['Text4']))

def shrineFilter(poi):
    if poi['id'] == 'Sign' or poi['id'] == 'minecraft:sign':
        if poi['Text1'] == '/marker' and poi['Text2'] == 'shrine':
            return '<b>' + escape('Schrein %s %s' % (poi['Text3'], poi['Text4'])) + '</b><br>- Teleportation<br>- Test<br>- Hallo Welt</ul>'

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
    'title': 'Welt 1',
    'rendermode': smooth_lighting,
    'dimension': 'overworld',
    'northdirection': 'upper-left',
    'showspawn': True,
    'markers': [
        dict(name='Heimatorte', checked=True, filterFunction=playerHomeFilter, icon='markers/marker_player_home.png'),
        #dict(name='Schreine', checked=True, filterFunction=shrineFilter, icon='markers/marker_shrine.png'),
        dict(name='Burgen', checked=True, filterFunction=castleFilter, icon='markers/marker_tower.png'),
        dict(name='Spieler', checked=False, filterFunction=playerIconsFilter)
    ],
    'center': [162, 80, -1463],
    'crop': (-2338, -3963, 2662, 1037)
}

defaultzoom = 3

texturepath = ''
customwebassets = './assets'
outputdir = './map'
