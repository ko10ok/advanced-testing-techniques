# Запуск окружения с параметризацией тестов

⚠️Не запускается тк не проверял поддержку установки env через init и нужно доработать проверку уникальности окружений

```shell
export COMPOSE_FILE=docker-compose.bootstrap.yml:docker-compose.e2e.yml:docker-compose.yml
```

### Подтянуть актуальные образы из CI
```shell
docker-compose pull | true
```

### Запустить bootstrap образы
```shell
docker-compose down
```
```shell
docker-compose up -d dockersock maxwelld e2e
```

### ⏩ Запустить тесты
```shell
docker-compose exec e2e python3 -m vedro run
```

### Не забыть потушить все контейнеры за собой
```shell
docker-compose down
```
