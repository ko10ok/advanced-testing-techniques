import vedro
from maxwelld import ComposeConfig
from maxwelld import DEFAULT_COMPOSE
from maxwelld import MaxwellDemonClient
from maxwelld import VedroMaxwell


class Config(vedro.Config):
    class Plugins(vedro.Config.Plugins):
        class VedroMaxwell(VedroMaxwell):
            enabled = True
            compose_cfgs = {
                DEFAULT_COMPOSE: ComposeConfig('docker-compose.yml', parallel_env_limit=1),
            }
            maxwell_demon_client = MaxwellDemonClient(host="http://maxwelld")
