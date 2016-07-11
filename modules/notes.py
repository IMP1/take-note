# -*- coding: utf-8 -*-
from gluon.html import * 
from gluon.dal import Row

def get_child_count(note):
    return db((db.note.parent == note.id) & (db.note.parent != db.note.id)).count()

def get_children(note):
    note_id = note
    if type(note) is Row:
        note_id = note.id
    return db((db.note.parent == note_id) & (db.note.parent != db.note.id)).select()

def get_moveable_notes(note):
    if isinstance(note, (long, int)):
        note = db.note(note)
    root_note = get_project(note)
    result = list()
    if root_note.id != note.id:
        result.append(db.note(note.parent))
        result.append(db.note(root_note.id))
    return get_other_branches(root_note, note, result)

def get_other_branches(root_note, note_to_avoid, result=None):
    if result == None:
        result = list()
    if root_note == note_to_avoid:
        return result
    children = get_children(root_note)
    for child in children:
        if not child in result and child != note_to_avoid:
            result.append(child)
        get_other_branches(child, note_to_avoid, result)
    return result

def get_parent(note):
    return db(db.note.id == note.parent).select().first()

def get_parents(note, result=None):
    if result == None:
        result = list()
    if (note.parent == note.id):
        return result
    else:
        parent = get_parent(note)
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

def get_contents_html(note):
    import re
    if isinstance(note, (long, int)):
        note = db.note(note)
    base_url = str(URL('project', 'view'))
    result = XML(re.sub(r"{((.+):)?(\d+)}", "<a href=\"" + base_url + r"/\3\">\2</a>", note.contents))
    return result

def get_contents_plain(note):
    import re
    if isinstance(note, (long, int)):
        note = db.note(note)
    base_url = str(URL('project', 'view'))
    result = re.sub(r"{((.+):)?\d+}", r"\2", note.contents)
    return result    