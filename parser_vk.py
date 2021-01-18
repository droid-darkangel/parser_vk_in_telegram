import requests


class Parser_vk_api:
    """
    Пример:
        {
        'id': 346954757, 'first_name': 'Владимир', 'last_name': 'Булгаков', 'is_closed': True,
        'can_access_closed': False, 'domain': 'vfangel', 'country': {'id': 19, 'title': 'Австралия'},
        'photo_50': 'https://sun1-94.userapi.com/impg/bSWt8x5rYL93ReY_j5ekkJLcUNbbBBb1ABf_lA/Ar0PY528Z4w.jpg?size=50x0&quality=88&crop=1,0,998,998&sign=8355170d64d6ba8168d7f1d2700cc985&c_uniq_tag=u2VnSZWCJsbNGioWanGyWbE0o30XWyCheaJRvHGak5I&ava=1',
        'has_mobile': 1, 'online': 0, 'status': '�💔\tА на меня всем пофиг, классно�💔',
        'verified': 0,
        'counters':
            {
            'albums': 0, 'videos': 0, 'audios': 0, 'friends': 877,
            'online_friends': 0, 'mutual_friends': 0, 'posts': 2256, 'subscriptions': 24
            'pages': 591
            }
        }
    """

    def __init__(self):
        self.api_token = '5e5a10df465ea56617dc6e2616f16e997c8df8f1059bc76c0ce83a5fcbaf113163be1f666cf47f59b6946'#это тестовый vk_токен хацкер
        self.api_url = 'https://api.vk.com/method/' 

    def get_user_info(self , user_id:str) -> dict:
        response = requests.get( self.api_url + 'users.get' , params={'user_ids':user_id  ,
                                                'fields':'photo_50,verified,online,status,citi,country,contacts,has_mobile,domain,counters',
                                                'access_token':self.api_token , 'v':5.124 })
        response_json = response.json()
        response_json = dict(response_json)['response'][0]

        return response_json
