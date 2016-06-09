# -*- coding: utf-8 -*-
from gluon.html import * 

def get_child_count(note):
    return db((db.note.parent == note.id) & (db.note.parent != db.note.id)).count()

def get_children(note):
    return db((db.note.parent == note.id) & (db.note.parent != db.note.id)).select()

def get_parents(note, result=None):
    if result == None:
        result = list()
    if (note.parent == note.id):
        return result
    else:
        parent = db(db.note.id == note.parent).select().first()
        result.insert(0, parent)
        return get_parents(parent, result)

def get_child_list_html(note):
    if get_child_count(note) > 0:
        children = list()
        for child in get_children(note):
            button = TAG.button(SPAN(_class="fa fa-caret-right"), _onclick='openNote(' + str(child.id) + ');')
            title = SPAN(child.title, _onclick='selectNote("' + child.title + '", "' + child.contents + '");')
            link = A(SPAN(_class="fa fa-link"), _href=URL('project', 'view', args=[child.id]))
            children.append(LI(button, title, link, get_child_list_html(child), _id="project-" + str(child.id)))
        return UL(*children)
    else:
        return ""

def get_children_contents(note, result=None):
    if result == None:
        result = list()
    if get_child_count(note) == 0:
        return []
    else:
        for child in get_children(note):
            result.append( (child.id, child.contents) )
            result.extend( get_children_contents(child) )
        return result

def get_project(note):
    if note.id == note.parent:
        return note
    else:
        parent = db(db.note.id == note.parent).select().first()
        return get_project(parent)