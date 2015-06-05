# -*- coding: utf-8 -*-

def get_child_count(note):
	return db((db.note.parent == note.id) & (db.note.parent != db.note.id)).count()

def get_children(note):
	return db((db.note.parent == note.id) & (db.note.parent != db.note.id)).select()
