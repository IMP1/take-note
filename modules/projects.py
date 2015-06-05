# -*- coding: utf-8 -*-

def get_count():
	return db(db.note.parent == db.note.id).count()

def get_projects():
	return db(db.note.parent == db.note.id).select()