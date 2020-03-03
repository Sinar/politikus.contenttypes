# -*- coding: utf-8 -*-
from plone.dexterity.content import Container
from collective import dexteritytextindexer
from plone.autoform.interfaces import IFormFieldProvider
from zope.interface import alsoProvides
from plone.supermodel import model
from zope import schema
from politikus.contenttypes import _
from zope.schema.vocabulary import SimpleVocabulary
from plone.indexer import indexer


class IIssue(model.Schema):
    """ Marker interface for Issue
    """

    dexteritytextindexer.searchable('whatever_categories')
    whatever_categories =  schema.Choice(
        title=_(u'Whatever Categories'),
        vocabulary=SimpleVocabulary.fromValues([_(u'foo'),_(u'bar'),_(u'far'),_(u'boo')]),
        required=False,
    )

    procurement_categories =  schema.Choice(
        title=_(u'Procurement categories'),
        vocabulary=SimpleVocabulary.fromValues([_(u'fun'),_(u'plate'),_(u'triste'),_(u'honteux')]),
        required=False,
    )
alsoProvides(IIssue, IFormFieldProvider)

@indexer(IIssue)
def procurementCategoriesIndexer(obj):
    return obj.procurement_categories
