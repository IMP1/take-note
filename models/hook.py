# -*- coding: utf-8 -*-
from gluon.custom_import import track_changes
track_changes(True)

import projects
projects.db = db

import notes
notes.db = db