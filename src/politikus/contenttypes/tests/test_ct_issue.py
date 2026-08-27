# -*- coding: utf-8 -*-
from plone import api
from plone.api.exc import InvalidParameterError
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.dexterity.interfaces import IDexterityFTI
from politikus.contenttypes.content.issue import IIssue
from politikus.contenttypes.testing import POLITIKUS_CONTENTTYPES_INTEGRATION_TESTING  # noqa
from zope.component import createObject
from zope.component import queryUtility

import unittest


class IssueIntegrationTest(unittest.TestCase):

    layer = POLITIKUS_CONTENTTYPES_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.parent = self.portal

    def test_ct_issue_schema(self):
        fti = queryUtility(IDexterityFTI, name='Issue')
        schema = fti.lookupSchema()
        self.assertIs(schema, IIssue)

    def test_ct_issue_fti(self):
        fti = queryUtility(IDexterityFTI, name='Issue')
        self.assertTrue(fti)

    def test_ct_issue_factory(self):
        fti = queryUtility(IDexterityFTI, name='Issue')
        factory = fti.factory
        obj = createObject(factory)


    def test_ct_issue_adding(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        obj = api.content.create(
            container=self.portal,
            type='Issue',
            id='issue',
        )


        parent = obj.__parent__
        self.assertIn('issue', parent.objectIds())

        # check that deleting the object works too
        api.content.delete(obj=obj)
        self.assertNotIn('issue', parent.objectIds())

    def test_ct_issue_globally_addable(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        fti = queryUtility(IDexterityFTI, name='Issue')
        self.assertTrue(
            fti.global_allow,
            u'{0} is not globally addable!'.format(fti.id)
        )

    def test_ct_issue_filter_content_type_true(self):
        # The Issue FTI filters content types; a Document is not in its
        # allowed_content_types and must be rejected.
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        fti = queryUtility(IDexterityFTI, name='Issue')
        portal_types = self.portal.portal_types
        parent_id = portal_types.constructContent(
            fti.id,
            self.portal,
            'issue_id',
            title='Issue container',
         )
        self.parent = self.portal[parent_id]
        with self.assertRaises(InvalidParameterError):
            api.content.create(
                container=self.parent,
                type='Document',
                title='My Content',
            )
