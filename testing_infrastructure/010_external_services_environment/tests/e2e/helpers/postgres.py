

def no_items():
    # DSN_DB уже содержит интерполированный c worker_id в DB name
    Postgres(environ.get('DSN_DB')).cleanup(md.services())
