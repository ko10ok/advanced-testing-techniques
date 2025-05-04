import httpx
import vedro
from maxwelld import Env
from maxwelld import Environment
from maxwelld import Service


class Scenario(vedro.Scenario):
    subject = 'with {param=} in {value}'
    vedro.params('FEATURE_ENABLE', 'true')
    vedro.params('FEATURE_ENABLE', 'false')
    vedro.params('FEATURE_ENABLE', '0')
    vedro.params('FEATURE_ENABLE', '')
    def __init__(self, param, value):
        env = Environment(   # для старого ведра tags = [Env...]
            'EnvEnabledFeatureName',  # будет не нужно после автоматического определения подходящих параметров и набора сервисов
            Service('app', Env({param: value})),
            Service('migrations'),
            Service('db'),
        )

    async def step(self):
        self.app_environment = httpx.get('http://app:8080/env').json()
        print(f'   ⌞ {self.app_environment["FEATURE_ENABLE"]=}')
        assert self.app_environment['FEATURE_ENABLE'] == 'true'
