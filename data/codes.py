import datetime
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Boolean
from sqlalchemy import orm
from .db_session import SqlAlchemyBase


class Code(SqlAlchemyBase):
    __tablename__ = "codes"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    key = Column(String, unique=True)
    code = Column(String)
    user_id = Column(Integer, ForeignKey("users_id"))
    user = orm.relation("User")
    created_date = Column(DateTime, default=datetime.datetime.now())
    visible = Column(Boolean, default=True)  # True if public, False if private
