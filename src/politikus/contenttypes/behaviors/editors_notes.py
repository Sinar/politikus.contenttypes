# -*- coding: utf-8 -*-

from politikus.contenttypes import _
from plone import schema
from plone.autoform.interfaces import IFormFieldProvider
from plone.supermodel import model
from Products.CMFPlone.utils import safe_hasattr
from zope.component import adapter
from zope.interface import Interface
from zope.interface import implementer
from plone.app.textfield import RichText
from plone.autoform import directives
from collective import dexteritytextindexer
from zope.interface import provider


class IEditorsNotesMarker(Interface):
    pass


@provider(IFormFieldProvider)
class IEditorsNotes(model.Schema):
    """
    """

    dexteritytextindexer.searchable('editors_notes')
    directives.read_permission(editors_notes='cmf.ModifyPortalContent')
    directives.write_permission(editors_notes='cmf.ModifyPortalContent')
    editors_notes = RichText(
        title=_(u'Editors Notes'),
        description=_(u'Notes viewable only for Editors'),
        required=False,
    )

@implementer(IEditorsNotes)
@adapter(IEditorsNotesMarker)
class EditorsNotes(object):
    def __init__(self, context):
        self.context = context

    @property
    def editors_notes(self):
        if safe_hasattr(self.context, 'editors_notes'):
            return self.context.editors_notes
        return None

    @editors_notes.setter
    def editors_notes(self, value):
        self.context.editors_notes = value
