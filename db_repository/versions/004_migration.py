from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
user = Table('user', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('name', String(length=20)),
    Column('password', String(length=20)),
    Column('s1', Boolean),
    Column('s2', Boolean),
    Column('s3', Boolean),
    Column('s4', Boolean),
    Column('role', SmallInteger, default=ColumnDefault(0)),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['user'].columns['s1'].create()
    post_meta.tables['user'].columns['s2'].create()
    post_meta.tables['user'].columns['s3'].create()
    post_meta.tables['user'].columns['s4'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['user'].columns['s1'].drop()
    post_meta.tables['user'].columns['s2'].drop()
    post_meta.tables['user'].columns['s3'].drop()
    post_meta.tables['user'].columns['s4'].drop()
