from datetime import datetime

from sqlalchemy import (
    Table, Column, String, Integer,
    TIMESTAMP, ForeignKey, MetaData, Float
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
    Column('score_id', ForeignKey('score.id'))
)

score = Table(
    'score',
    metadata,
    Column('id', Integer, autoincrement=True, primary_key=True),
    Column('cash', Float, default=0, lte=0),
    Column('SMS', Integer, default=0, lte=0),
    Column('internet', Integer, default=0, lte=0),
    Column('minute', Integer, default=0, lte=0),
)


userdata = Table(
    'userdata',
    metadata,
    Column('id', Integer, autoincrement=True, primary_key=True),
    Column('name', String, nullable=True),
    Column('email', String),
)

user_phone = Table(
    'user_phone',
    metadata,
    Column('id', Integer, autoincrement=True, primary_key=True),
    Column('user_id', ForeignKey('userdata.id')),
    Column('phone_id', ForeignKey('subscriber.id'))
)

package = Table(
    'package',
    metadata,
    Column('id', autoincrement=True, primary_key=True),
    Column('name', String),
    Column('SMS', Integer, default=0, lte=0),
    Column('internet', Integer, default=0, lte=0),
    Column('minute', Integer, default=0, lte=0),
    Column('expires_at', TIMESTAMP)
)

tariff = Table(
    'tariff',
    metadata,
    Column('id', autoincrement=True, primary_key=True),
    Column('name', String),
    Column('price', Float),
    Column('SMS', Integer, default=0, lte=0),
    Column('internet', Integer, default=0, lte=0),
    Column('minute', Integer, default=0, lte=0),
    Column('expires_at', TIMESTAMP),
)

additional = Table(
    'additional',
    metadata,
    Column('id', autoincrement=True, primary_key=True),
    Column('tariff_id', ForeignKey('tariff.id')),

)




