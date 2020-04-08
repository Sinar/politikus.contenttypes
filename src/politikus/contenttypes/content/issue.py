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

from z3c.relationfield.schema import RelationChoice
from plone.app.vocabularies.catalog import CatalogSource
from plone.app.z3cform.widget import RelatedItemsFieldWidget
from plone.autoform import directives

class IIssue(model.Schema):
    """ Marker interface for Issue
    """

    # Implicated Persons 
    directives.widget('implicated',
                      RelatedItemsFieldWidget,
                      pattern_options={
                        'mode': 'auto',
                        'favourites': [],
                        }
                      )

    implicated = RelationChoice(
            title=u'Implicated',
            source=CatalogSource(portal_type='Person'),
            required=False,
            )


@implementer(IIssue)
class Issue(Container):
    """
    """


