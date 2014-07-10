from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
survey1 = Table('survey1', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('userid', String),
    Column('gender', String),
    Column('age', String),
    Column('education', String),
    Column('education_O', String),
    Column('language', String(length=20)),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['survey1'].columns['education_O'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['survey1'].columns['education_O'].drop()
