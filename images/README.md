# Собрать все необходимые образы для демо

## Собрать все образы
```shell
docker buildx bake --load
```

## Для обновления на свежие версии зависимостей e2e
```shell
pip-compile -U e2e/requirements.in > e2e/requirements.txt
```
