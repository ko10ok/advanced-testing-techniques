import httpx
import vedro
from uber_compose import Env
from uber_compose import Environment
from uber_compose import Service


class Scenario(vedro.Scenario):
    env = Environment(   # для старого ведра tags = [Env...]
        Service('app', Env({'FEATURE_ENABLE': 'true'})),
        Service('migrations'),
        Service('db'),
        description='EnvEnabledFeatureName',
    )

    async def step(self):
        self.app_environment = httpx.get('http://app:8080/env').json()
        print(f'   ⌞ {self.app_environment["FEATURE_ENABLE"]=}')
        assert self.app_environment['FEATURE_ENABLE'] == 'true'
