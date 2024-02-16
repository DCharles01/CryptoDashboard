from settings import DATABASE_URL
import api.models.models as models
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create the tables in the database
# models.Base.metadata.create_all(bind=engine)

def create_crypto(symbol: str):

    # Create a new session
    db = SessionLocal()
    try:
        cryptocurrency = models.Cryptocurrency(symbol='bitcoin')
        # Add the User instance to the session
        db.add(cryptocurrency)
        # Commit the session to save the changes to the database
        db.commit()
        # Refresh the crypto instance to reflect the database changes
        db.refresh(cryptocurrency)
        return cryptocurrency
    finally:
        # Close the session
        db.close()


def delete_crypto(crypto_id):
    # Create a new session
    db = SessionLocal()
    try:

        crypto = db.query(models.Cryptocurrency).filter(models.Cryptocurrency.id == crypto_id).first()
        if crypto:

            db.delete(crypto)

            db.commit()
            return True
        else:
            return False
    finally:

        db.close()


def drop_all_tables():
    # Drop all tables defined in Base
    models.Base.metadata.drop_all(engine)
    print("All tables dropped successfully.")


# Example usage:
# deleted = delete_crypto(crypto_id==1)

