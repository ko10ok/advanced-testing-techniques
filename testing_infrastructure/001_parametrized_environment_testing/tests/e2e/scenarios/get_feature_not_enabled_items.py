import httpx
import vedro
from maxwelld import Env
from maxwelld import Environment
from maxwelld import Service


class Scenario(vedro.Scenario):
    env = Environment(   # для старого ведра tags = [Env...]
        'EnvDisabledFeatureName',  # будет не нужно после автоматического определения подходящих параметров и набора сервисов
        Service('app', Env({'FEATURE_ENABLE': 'false'})),
        Service('migrations'),
        Service('db'),
    )

    async def step(self):
        self.app_environment = httpx.get('http://app:8080/env').json()
        print(f'  ⌞ {self.app_environment["FEATURE_ENABLE"]=}')
        assert self.app_environment['FEATURE_ENABLE'] == 'false'
