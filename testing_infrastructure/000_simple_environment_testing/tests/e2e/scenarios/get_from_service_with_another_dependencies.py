import httpx
import vedro
from uber_compose import Environment
from uber_compose import Service


vedro.skip()
class Scenario(vedro.Scenario):
    env = Environment(   # для старого ведра tags = [Env...]
        Service('app'),
        Service('migrations'),
        Service('kafka'),
        Service('db'),
        description='EnvEnabledFeatureName',
    )

    async def step(self):
        self.app_environment = httpx.get('http://dockersock:2375/v1.40/containers/json').json()
        for container in self.app_environment:
            if container['Image'] == 'bitnami/kafka:3.2.3':
                assert container['State'] == 'running'
