import src.core.config as config
from sqlalchemy import create_engine    
from sqlalchemy.orm import declarative_base, sessionmaker

# knows how to connect to the database and create sessions
engine = create_engine(
    config.DATABASE_URL
    , pool_size=10
    , max_overflow=20
)

# factory for creating new Session objects
sessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# create a base class for our models to inherit from
base = declarative_base()