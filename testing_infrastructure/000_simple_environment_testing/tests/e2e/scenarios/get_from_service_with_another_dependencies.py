import httpx
import vedro
from maxwelld import Environment
from maxwelld import Service


vedro.skip()
class Scenario(vedro.Scenario):
    env = Environment(   # для старого ведра tags = [Env...]
        'EnvEnabledFeatureName',  # будет не нужно после автоматического определения подходящих параметров и набора сервисов
        Service('app'),
        Service('migrations'),
        Service('kafka'),
        Service('db'),
    )

    async def step(self):
        self.app_environment = httpx.get('http://app:8080/env').json()
        assert self.app_environment['FEATURE_ENABLE'] == 'true'
