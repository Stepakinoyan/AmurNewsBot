from sqlmodel import SQLModel, Field


class Users(SQLModel, table=True):
    id: int = Field(nullable=False, primary_key=True)
    tg_id: int = Field(unique=True)
