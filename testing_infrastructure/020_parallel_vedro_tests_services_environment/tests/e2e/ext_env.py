from maxwelld import Env

from env import app
from maxwelld import ExternalSerivce

kafka_ext = ExternalSerivce(kafka, Environment(
    app.with_env(
        Env({'KAFKA_BROKERS': 'kafka.dev'})
    ),
    e2e.with_env(
        Env({'KAFKA_BROKERS': 'kafka.dev'})
    )
))

postgres_db_ext = ExternalSerivce(postgres_db, Environment(
    EveryService().with_env(  # app migrations e2e
        Env({'DSN_DB': 'postgresql://app_user:app_password@postgres.dev:5432/app_db%(worker_id)?sslmode=disable'})
    )
))
