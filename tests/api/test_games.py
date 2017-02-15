import json

import responses

from twitch.client import TwitchClient
from twitch.resources import Game

example_top_games_response = {
   '_total': 1157,
   'top': [
      {
         'channels': 953,
         'viewers': 171708,
         'game': {
            '_id': 32399,
            'box': {
               'large': ('https://static-cdn.jtvnw.net/ttv-boxart/'
                         'Counter-Strike:%20Global%20Offensive-272x380.jpg'),
               'medium': ('https://static-cdn.jtvnw.net/ttv-boxart/'
                          'Counter-Strike:%20Global%20Offensive-136x190.jpg'),
               'small': ('https://static-cdn.jtvnw.net/ttv-boxart/'
                         'Counter-Strike:%20Global%20Offensive-52x72.jpg'),
               'template': ('https://static-cdn.jtvnw.net/ttv-boxart/Counter-St'
                            'rike:%20Global%20Offensive-{width}x{height}.jpg')
            },
            'giantbomb_id': 36113,
            'logo': {
               'large': ('https://static-cdn.jtvnw.net/ttv-logoart/'
                         'Counter-Strike:%20Global%20Offensive-240x144.jpg'),
               'medium': ('https://static-cdn.jtvnw.net/ttv-logoart/'
                          'Counter-Strike:%20Global%20Offensive-120x72.jpg'),
               'small': ('https://static-cdn.jtvnw.net/ttv-logoart/'
                         'Counter-Strike:%20Global%20Offensive-60x36.jpg'),
               'template': ('https://static-cdn.jtvnw.net/ttv-logoart/Counter-'
                            'Strike:%20Global%20Offensive-{width}x{height}.jpg')
            },
            'name': 'Counter-Strike: Global Offensive',
            'popularity': 170487
         }
      },
   ]
}


@responses.activate
def test_my_api():
    responses.add(responses.GET,
                  'https://api.twitch.tv/kraken/games/top',
                  body=json.dumps(example_top_games_response),
                  status=200,
                  content_type='application/json')

    client = TwitchClient('abcd')

    games = client.games.get_top()

    assert len(responses.calls) == 1
    assert len(games) == 1
    assert isinstance(games[0], Game)
