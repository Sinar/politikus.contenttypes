# -*- coding: utf-8 -*-

from plone.dexterity.browser.view import DefaultView
from politikus.contenttypes import _


# from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile


class IssueSourceView(DefaultView):
    # If you want to define a template here, please remove the template from
    # the configure.zcml registration of this view.
    # template = ViewPageTemplateFile('issue_source_view.pt')

    def __call__(self):
        return super(IssueSourceView, self).__call__()
