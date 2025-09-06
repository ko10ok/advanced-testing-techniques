from maxwelld import Env
from maxwelld import Environment
from maxwelld import Service


# from maxwelld import SingletonService
class SingletonService(Service):
    ...


app = Service('app')
migrations = Service('migrations')
postgres_db = SingletonService('postgres_db')  # SingletonService обозначает что будет поднят единственный инстанс
kafka = SingletonService('kafka')              # на все потоки параллельно запущенных тестов

EnvEnabledFeatureEnvironment = Environment(
    'EnvEnabledFeatureName', # будет не нужно после автоматического определения подходящих параметров и набора сервисов
    app.with_env(Env({'FEATURE_ENABLED': 'true'})), migrations, postgres_db, kafka
)

EnvDisabledFeatureEnvironment = Environment(
    'EnvDisabledFeatureName', # будет не нужно после автоматического определения подходящих параметров и набора сервисов
    app.with_env(Env({'FEATURE_ENABLED': 'false'})), migrations, postgres_db, kafka
)
