

def no_items():
    Postgres(environ.get('DSN_DB')).cleanup(md.services())  # DSN_DB уже содержит интерполированный c worker_id DB name
