# -*- coding: utf-8 -*-

# from politikus.contenttypes import _
# from Products.Five.browser import BrowserView
from plone.dexterity.browser.view import DefaultView
from zope.security import checkPermission

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
        # returns list of Issue Sources objects

        sources = self.context.listFolderContents(contentFilter={
            "portal_type": "Issue Source"
            })
        return sources
