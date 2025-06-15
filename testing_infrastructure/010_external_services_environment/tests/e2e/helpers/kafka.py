from env import kafka
from uber_compose import worker_instance
from d42 import fake
from schemas import TopicName
from kafka import KafkaApi


def generated_topic():
    name = fake(TopicName)
    # для динамических объектов требуется явно использовать поддержку уникальности для шаренных ресурсов
    return KafkaApi(kafka.instance()).new_topic(name=worker_instance(name))  # ... + vedro.worker_id()
