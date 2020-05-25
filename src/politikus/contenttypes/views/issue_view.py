# -*- coding: utf-8 -*-

# from politikus.contenttypes import _
# from Products.Five.browser import BrowserView

from Acquisition import aq_inner
from zope.component import getUtility
from zope.intid.interfaces import IIntIds
from zope.security import checkPermission
from zc.relation.interfaces import ICatalog
from zope.schema.interfaces import IVocabularyFactory
from plone.dexterity.browser.view import DefaultView

# from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile


class IssueView(DefaultView):
    # If you want to define a template here, please remove the template from
    # the configure.zcml registration of this view.
    # template = ViewPageTemplateFile('issue_view.pt')

    def __call__(self):
        # Implement your own actions:
        return super(IssueView, self).__call__()

    def can_editor_view(self):
        return checkPermission('cmf.ModifyPortalContent', self.context)

    def source_timeline(self):
        """
        Return back references from source object on specified attribute_name
        """
        catalog = getUtility(ICatalog)
        intids = getUtility(IIntIds)

        source_object = self.context
        attribute_name = 'issue'

        result = []

        for rel in catalog.findRelations(
            dict(to_id=intids.getId(aq_inner(source_object)),
                 from_attribute=attribute_name)
              ):

            obj = intids.queryObject(rel.from_id)

            if obj is not None and checkPermission('zope2.View', obj):
                if obj.portal_type == 'Issue Source':
                    result.append(obj)

        return result
