from src.db.database import sessionLocal

def get_db():
    """Dependency that provides a database session."""
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()