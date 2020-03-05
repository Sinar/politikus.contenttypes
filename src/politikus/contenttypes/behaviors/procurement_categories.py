# -*- coding: utf-8 -*-

from politikus.contenttypes import _
from plone import schema
from plone.autoform.interfaces import IFormFieldProvider
from plone.supermodel import model
from Products.CMFPlone.utils import safe_hasattr
from zope.component import adapter
from zope.interface import Interface
from zope.interface import implementer
from zope.interface import provider
from zope.schema.vocabulary import SimpleVocabulary
from collective.dexteritytextindexer.utils import searchable


class IProcurementCategoriesMarker(Interface):
    pass


@provider(IFormFieldProvider)
class IProcurementCategories(model.Schema):
    """
    """
    procurement_categories = schema.Choice(
        title=_(u'Procurement categories'),
        vocabulary=SimpleVocabulary.fromValues([_(u'fun'), _(u'plate'),
                                                _(u'triste'), _(u'honteux')]),
        required=False,
    )


searchable(IProcurementCategories, 'procurement_categories')


@implementer(IProcurementCategories)
@adapter(IProcurementCategoriesMarker)
class ProcurementCategories(object):
    def __init__(self, context):
        self.context = context

    @property
    def procurement_categories(self):
        if safe_hasattr(self.context, 'procurement_categories'):
            return self.context.procurement_categories
        return None

    @procurement_categories.setter
    def procurement_categories(self, value):
        self.context.procurement_categories = value
