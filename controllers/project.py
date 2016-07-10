# -*- coding: utf-8 -*-
import notes

def create():
    response.title = "New Project - Take Note"
    form = SQLFORM(db.note)
    if form.validate(formname='new-project'):
        id = db.note.insert(title=form.vars.title, contents=form.vars.contents)
        row = db(db.note.id==id).select().first()
        row.update_record(parent=id)
        redirect(URL('project', 'view', args=[id]))
    return dict(form=form, formkey = form.formkey)

def view():
    form = SQLFORM(db.note)
    if form.validate(formname='new-note'):
        db.note.insert(title=form.vars.title, contents=form.vars.contents, parent=form.vars.parent)
        redirect()
    note = db(db.note.id == request.args[0]).select().first()
    return dict(form=form, formkey = form.formkey, note=note)

def overview():
    note = db(db.note.id == request.args[0]).select().first()
    project = notes.get_project(note)
    return dict(project=project)

def index():
    redirect(URL('default', 'index'))

def edit():
    id = request.vars.id
    new_title = request.vars.title
    new_desc = request.vars.description
    db.note(id).update_record(title=new_title, contents=new_desc)
    return DIV(H1(new_title), P(new_desc))

def insert():
    note_id = request.vars.id
    children = notes.get_children(note_id)
    new_parent = db.note.insert(title=request.vars.title, contents=request.vars.description, parent=note_id)
    for child in children:
        db.note(child.id).update_record(parent=new_parent)
    return new_parent

def move():
    id = request.vars.id
    new_parent = request.vars.parent
    db.note(id).update_record(parent=new_parent)