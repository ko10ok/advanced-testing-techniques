import httpx
import vedro

from env import EnvDisabledFeatureEnvironment
from helpers.kafka import generated_topic
from helpers.postgres import no_items


class Scenario(vedro.Scenario):
    seld.env = EnvDisabledFeatureEnvironment

    async def no_db_items(self):
        no_items()

    async def new_topic(self):
        self.topic = generated_topic()

    async def step(self):
        self.app_environment = httpx.get('http://app:8080/env').json()
        print(f'   ⌞ {self.app_environment["FEATURE_ENABLE"]=}')
        assert self.app_environment['FEATURE_ENABLE'] == 'true'
