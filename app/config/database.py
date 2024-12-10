from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from contextlib import contextmanager

db_user = "root"
db_password = ""
db_host = "localhost"
db_port = "3306"
db_name = "meubanco"

DATABASE_URL = f"mysql+pymysql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"

db = create_engine(DATABASE_URL)

try:
    with db.connect() as connection:
        print("Conexão bem-sucedida!")
except Exception as e:
    print(f"Erro ao conectar ao banco de dados: {e}")
    print(str(e))

Session = sessionmaker(bind=db)
session = Session()

@contextmanager
def get_db():
    db = Session()
    try:
        yield db
        db.commit()
    except Exception as e:
        db.rollback()
        print(f"Erro na transação: {e}")
        raise e
    finally:
        db.close()





