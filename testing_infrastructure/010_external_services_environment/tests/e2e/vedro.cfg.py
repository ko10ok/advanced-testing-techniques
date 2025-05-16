import vedro
from maxwelld import ComposeConfig
from maxwelld import DEFAULT_COMPOSE
from maxwelld import ExternalSerivce
from maxwelld import Environment
from maxwelld import MaxwellDemonClient
from maxwelld import VedroMaxwell
from ext_env import kafka_ext, postgres_db_ext


class Config(vedro.Config):
    class Plugins(vedro.Config.Plugins):
        class VedroMaxwell(VedroMaxwell):
            enabled = True
            compose_cfgs = {
                DEFAULT_COMPOSE: ComposeConfig(
                    'docker-compose.yml', parallel_env_limit=1,
                    services_override=[kafka_ext, postgres_db_ext]
                )
            }
            maxwell_demon_client = MaxwellDemonClient(host="http://maxwelld")
