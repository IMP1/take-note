# -*- coding: utf-8 -*-
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
    project = db(db.note.id == request.args[0]).select().first()
    return dict(project=project)