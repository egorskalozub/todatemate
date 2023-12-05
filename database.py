import config
from sqlalchemy import create_engine

engine = create_engine(config.DATABASE_URI)

def get_user(user_id):
    # Database query to get user
    pass

# Other database functions
