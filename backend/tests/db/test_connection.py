import pytest
import api.models.models as models
from db.sqlalchemy_engine import engine
from sqlalchemy.orm import sessionmaker

@pytest.fixture
def db_engine():
    models.Base.metadata.drop_all(engine)
    models.Base.metadata.create_all(bind=engine)
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    cryptocurrency = models.Cryptocurrency(symbol='bitcoin')

    db = SessionLocal()

    db.add(cryptocurrency)

    db.commit()

    # Refresh the crypto instance to reflect the database changes
    # db.refresh(cryptocurrency)

    # breakpoint()

    yield engine

    # tear down
    models.Base.metadata.drop_all(engine)
    engine.dispose()
    db.close()

@pytest.fixture
def db_connection(db_engine):
    connection = db_engine.connect()
    yield connection
    connection.close()

def test_db_connection_successful(db_connection):
    assert db_connection is not None

def test_cryptocurrencies_has_record_bitcoin(db_connection):
    # breakpoint()
    conn = db_connection.connection

    cursor = conn.cursor()
    # breakpoint()
    # Execute the SQL query using the connection object
    cursor.execute("select * from cryptocurrencies")

    rows = cursor.fetchall()
    assert len(rows) == 1
    # breakpoint()
    assert rows[0][1] == 'bitcoin'
