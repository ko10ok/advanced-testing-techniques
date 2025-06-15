# Разные параметры окружения для разных тестов

## Запуск

```shell
export COMPOSE_FILE=docker-compose.e2e.yml
```

### Подтянуть актуальные образы из CI
```shell
docker-compose pull | true
```

### Запустить bootstrap образы
```shell
docker-compose down
docker-compose up -d dockersock e2e
```

### ⏩ Запустить тесты
```shell
docker-compose exec e2e python3 -m vedro run
```
с подробностями запуска
```shell
docker-compose exec e2e python3 -m vedro run --uc-v
```
или для отладки 
с подробностями запуска
```shell
docker-compose exec e2e python3 -m vedro run --uc-v DEBUG
```


### Не забыть потушить все контейнеры за собой
```shell
docker-compose down
```
