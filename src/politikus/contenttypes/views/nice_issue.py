# -*- coding: utf-8 -*-

from politikus.contenttypes import _
from plone.dexterity.browser.view import DefaultView

# from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile


class NiceIssue(DefaultView):
    # If you want to define a template here, please remove the template from
    # the configure.zcml registration of this view.
    # template = ViewPageTemplateFile('nice_issue.pt')

    def __call__(self):
        # Implement your own actions:
        return super(NiceIssue, self).__call__()
