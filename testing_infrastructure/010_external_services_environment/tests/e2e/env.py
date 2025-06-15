from uber_compose import Environment
from uber_compose import Service


app = Service('app')
migrations = Service('migrations')
postgres_db = Service('postgres_db')
kafka = Service('kafka')

FullEnvironment = Environment(
    'EnvEnabledFeatureName', # будет не нужно после автоматического определения подходящих параметров и набора сервисов

    # можно использовать/реализовать для набора EveryService генератор из maxwelld
    app, migrations, postgres_db, kafka,
)
