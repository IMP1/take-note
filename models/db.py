# -*- coding: utf-8 -*-

db = DAL('sqlite://storage.db')

#
db.define_table('note',
        Field('title', 'string', requires=[IS_NOT_EMPTY()]),
        Field('contents', 'text', requires=[]),
        Field('parent', 'reference note'),
    )
