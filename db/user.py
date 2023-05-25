from datetime import datetime

from sqlalchemy import TIMESTAMP, VARCHAR, Column, Integer

from .base import BaseModel


class User(BaseModel):
    """
    :user_id: `Column` telegram uid
    :username: `Column` telegram username
    :interaction: `Column` last user interaction
    """

    __tablename__ = "users"

    # Telegram UID
    user_id = Column(Integer, unique=True, nullable=False, primary_key=True)

    # Telegram Username
    username = Column(VARCHAR(32), unique=False, nullable=True)

    # Interaction
    interaction = Column(VARCHAR(8), unique=False, nullable=True)

    # Start date
    start_date = Column(TIMESTAMP, default=(datetime.now().replace(microsecond=0)))

    # Last interaction date
    upd_date = Column(TIMESTAMP, onupdate=(datetime.now().replace(microsecond=0)))

    def __str__(self) -> str:
        return f"<User: {self.user_id}>"
