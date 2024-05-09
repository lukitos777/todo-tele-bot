from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Task(Base):
    __tablename__ = 'Tasks'
    id = Column(Integer, primary_key=True, autoincrement=True)
    data = Column(DateTime, nullable=False)
    title = Column(String(75), nullable=False)
    task = Column(String(200), nullable=False)

# it's a model for database:
#
# id   |data   |title   |task   |
# -----+-------+--------+-------+
# 1    |UTC    |str     |str    |
# -----+-------+--------+-------+