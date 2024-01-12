from datetime import datetime
import enum

from sqlalchemy import (
    Table, Column, Text, String, Integer, Boolean, TIMESTAMP, ForeignKey, Enum, MetaData, Float
)

metadata = MetaData()

subscriber = Table(
    'subscriber',
    metadata,
    Column('id', Integer, autoincrement=True, primary_key=True),
    Column('firstname', String, max_length=50),
    Column('lastname', String, max_length=50),
    Column('patronymic', String, max_length=50),
    Column('phone', String, max_length=13),
    Column('PINFL', Integer),
    Column('passport_series', String),
    Column('passport_address', String),
    Column('birthday', TIMESTAMP),
    Column('created_at', TIMESTAMP, default=datetime.utcnow()),

)


userdata = Table(
    'userdata',
    metadata,
    Column('id', Integer, autoincrement=True, primary_key=True),
    Column('name', String, nullable=True),
    Column('email', String),
    Column('')

)



