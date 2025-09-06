from env import kafka
from maxwelld import worker_instance
from d42 import fake
from schemas import TopicName
from kafka import KafkaApi


def generated_topic():
    name = fake(TopicName)
    return KafkaApi(kafka.instance()).new_topic(name=worker_instance(name))  # ... + vedro.worker_id()
