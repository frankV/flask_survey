from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
survey3 = Table('survey3', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('userid', VARCHAR),
    Column('choose_names', BOOLEAN),
    Column('choose_numbers', BOOLEAN),
    Column('choose_songs', BOOLEAN),
    Column('choose_mnemonic', BOOLEAN),
    Column('choose_sports', BOOLEAN),
    Column('choose_famous', BOOLEAN),
    Column('choose_words', BOOLEAN),
    Column('secure_numbers', BOOLEAN),
    Column('secure_upper_case', BOOLEAN),
    Column('secure_symbols', BOOLEAN),
    Column('secure_eight_chars', BOOLEAN),
    Column('secure_no_dict', BOOLEAN),
    Column('secure_adjacent', BOOLEAN),
    Column('secure_nothing', BOOLEAN),
    Column('modify', VARCHAR),
    Column('usedPassword', VARCHAR),
    Column('wordPart', VARCHAR),
    Column('number_N', BOOLEAN),
    Column('number_added_digits', BOOLEAN),
    Column('number_deleted_digits', BOOLEAN),
    Column('number_substituted_digits', BOOLEAN),
    Column('number_O', VARCHAR),
    Column('char_N', BOOLEAN),
    Column('char_added_symbols', BOOLEAN),
    Column('char_deleted_symbols', BOOLEAN),
    Column('char_substituted_symbols', BOOLEAN),
    Column('char_O', VARCHAR),
)

survey3 = Table('survey3', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('userid', String),
    Column('choose_names', Boolean),
    Column('choose_numbers', Boolean),
    Column('choose_songs', Boolean),
    Column('choose_mnemonic', Boolean),
    Column('choose_sports', Boolean),
    Column('choose_famous', Boolean),
    Column('choose_words', Boolean),
    Column('choose_O', String),
    Column('secure_numbers', Boolean),
    Column('secure_upper_case', Boolean),
    Column('secure_symbols', Boolean),
    Column('secure_eight_chars', Boolean),
    Column('secure_no_dict', Boolean),
    Column('secure_adjacent', Boolean),
    Column('secure_nothing', Boolean),
    Column('secure_O', String),
    Column('modify', String),
    Column('usedPassword', String),
    Column('word_part_N', Boolean),
    Column('word_part_changed_completely', Boolean),
    Column('word_part_changed_slightly', Boolean),
    Column('word_part_capitalized_letters', Boolean),
    Column('word_part_O', String),
    Column('number_N', Boolean),
    Column('number_added_digits', Boolean),
    Column('number_deleted_digits', Boolean),
    Column('number_substituted_digits', Boolean),
    Column('number_O', String),
    Column('char_N', Boolean),
    Column('char_added_symbols', Boolean),
    Column('char_deleted_symbols', Boolean),
    Column('char_substituted_symbols', Boolean),
    Column('char_O', String),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['survey3'].columns['wordPart'].drop()
    post_meta.tables['survey3'].columns['choose_O'].create()
    post_meta.tables['survey3'].columns['secure_O'].create()
    post_meta.tables['survey3'].columns['word_part_N'].create()
    post_meta.tables['survey3'].columns['word_part_O'].create()
    post_meta.tables['survey3'].columns['word_part_capitalized_letters'].create()
    post_meta.tables['survey3'].columns['word_part_changed_completely'].create()
    post_meta.tables['survey3'].columns['word_part_changed_slightly'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['survey3'].columns['wordPart'].create()
    post_meta.tables['survey3'].columns['choose_O'].drop()
    post_meta.tables['survey3'].columns['secure_O'].drop()
    post_meta.tables['survey3'].columns['word_part_N'].drop()
    post_meta.tables['survey3'].columns['word_part_O'].drop()
    post_meta.tables['survey3'].columns['word_part_capitalized_letters'].drop()
    post_meta.tables['survey3'].columns['word_part_changed_completely'].drop()
    post_meta.tables['survey3'].columns['word_part_changed_slightly'].drop()
