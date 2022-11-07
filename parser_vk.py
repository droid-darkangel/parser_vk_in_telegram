import requests


class Parser_vk_api:
    def __init__(self):
        self.api_token = '5e5a10df465ea56617dc6e2616f16e997c8df8f1059bc76c0ce83a5fcbaf113163be1f666cf47f59b6946'#это тестовый vk токен
        self.api_url = 'https://api.vk.com/method/' 

    def get_user_info(self , user_id:str) -> dict:
        response = requests.get( self.api_url + 'users.get' , params={'user_ids':user_id  ,
                                                'fields':'photo_50,verified,online,status,citi,country,contacts,has_mobile,domain,counters',
                                                'access_token':self.api_token , 'v':5.124 })
        response_json = response.json()
        response_json = dict(response_json)['response'][0]

        return response_json
