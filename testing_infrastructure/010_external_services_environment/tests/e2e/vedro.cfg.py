import vedro
from uber_compose import ComposeConfig
from uber_compose import DEFAULT_COMPOSE
from uber_compose import Env
from uber_compose import Service
from uber_compose import VedroUberCompose
from uber_compose import OverridenService

from env import kafka
from env import postgres_db


class Config(vedro.Config):
    class Plugins(vedro.Config.Plugins):
        class VedroUberCompose(VedroUberCompose):
            enabled = True
            compose_cfgs = {
                DEFAULT_COMPOSE: ComposeConfig(
                    'docker-compose.yml', parallel_env_limit=1,
                    overridden_services=[
                        OverridenService(
                            kafka,
                            [Service('app', Env({'BOOTSTRAP_SERVER': 'kafka.external.dev'}))]
                        ),
                        OverridenService(
                            postgres_db,
                            [
                                Service('app', Env({
                                    'DSN_DB': 'postgresql://app_user:app_password@'
                                              'postgres.dev:5432/app_db%(worker_id)?sslmode=disable'
                                }))
                            ]
                        )
                    ]
                )
            }
