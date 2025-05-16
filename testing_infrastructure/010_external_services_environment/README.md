# Запуск окружения с использованием шаренных внешних сервисов

⚠️ пример не запускается тк нужен инстанс внешней кафки и pg + доработку и отладку реализации в менеджере окружений + тесты

Пр запуске с параметром вместо локальных сервисов `kafka` и `postgres_db` в остальных сервисах подмениться ENV и конфиги для использования внешнего сервиса и учетом уникального id потока сервиса

**При подмене сервисов нужно параметризовать**
- ENV для приложения
- конфиг файлы приложения (⚠ нет реализации)
- ENV для тестов
- шаги миграций и предустановок
- контексты тестов/интерфейсов взаимодействия с подмененными сервисами

## Запуск
### Подтянуть актуальные образы из CI и поднять bootsrap
```shell
docker-compose pull | true
docker-compose down
docker-compose up -d dockersock maxwelld e2e
```

### ⏩ Запустить тесты использую переопределенные параметры сервиса

```shell
docker-compose exec e2e python3 -m vedro run --md-services-override [ by default ALL ]
```

```shell
docker-compose exec e2e python3 -m vedro run --md-services-override=kafka
```

```shell
docker-compose exec e2e python3 -m vedro run --md-services-override=kafka,postgres_db
```
