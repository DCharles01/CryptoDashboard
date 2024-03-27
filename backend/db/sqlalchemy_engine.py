from .settings import DATABASE_URL, TEST_DATABASE_URL, DEV_DATABASE_URL
from sqlalchemy import create_engine
import api.models.models as models

engine = create_engine(DATABASE_URL)
# test_engine = create_engine(TEST_DATABASE_URL)
# dev_engine = create_engine(DEV_DATABASE_URL)