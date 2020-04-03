# -*- coding: utf-8 -*-
from plone.dexterity.content import Container
from collective import dexteritytextindexer
from plone.autoform.interfaces import IFormFieldProvider
from zope.interface import alsoProvides
from plone.supermodel import model
from zope import schema
from politikus.contenttypes import _
from zope.schema.vocabulary import SimpleVocabulary
from zope.interface import implementer
from plone.indexer import indexer
from collective import dexteritytextindexer


class IIssue(model.Schema):
    """ Marker interface for Issue
    """

@implementer(IIssue)
class Issue(Container):
    """
    """


