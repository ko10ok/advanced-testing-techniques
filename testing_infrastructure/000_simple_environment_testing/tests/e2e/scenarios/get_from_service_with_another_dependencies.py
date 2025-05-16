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
        self.app_environment = httpx.get('http://dockersock:2375/v1.40/containers/json').json()
        for container in self.app_environment:
            if container['Image'] == 'bitnami/kafka:3.2.3':
                assert container['State'] == 'running'
