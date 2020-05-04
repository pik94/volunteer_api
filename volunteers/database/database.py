from pathlib import Path

from flask_sqlalchemy import SQLAlchemy

from volunteers import config as cfg


db = SQLAlchemy()


def get_connection_string() -> str:
    if cfg.DB_TYPE == 'postgresql':
        s = (f'postgresql+psycopg2://{cfg.DB_USER}:{cfg.DB_PASSWORD}@'
             f'{cfg.DB_HOST}:{cfg.DB_PORT}/{cfg.DB_NAME}')
    elif cfg.DB_TYPE == 'sqlite':
        db_path = Path(cfg.DB_NAME).absolute()
        s = f'sqlite:///{db_path}'
    else:
        raise RuntimeError(f'Unknown DB type {cfg.DB_TYPE}')
    return s
