# -*- coding: utf-8 -*-
from plone import api
from plone.api.exc import InvalidParameterError
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.dexterity.interfaces import IDexterityFTI
from politikus.contenttypes.content.issue_source import IIssueSource  # NOQA E501
from politikus.contenttypes.testing import POLITIKUS_CONTENTTYPES_INTEGRATION_TESTING  # noqa
from zope.component import createObject
from zope.component import queryUtility

import unittest


class IssueSourceIntegrationTest(unittest.TestCase):

    layer = POLITIKUS_CONTENTTYPES_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        portal_types = self.portal.portal_types
        parent_id = portal_types.constructContent(
            'Issue',
            self.portal,
            'parent_container',
            title='Parent container',
        )
        self.parent = self.portal[parent_id]

    def test_ct_issue_source_schema(self):
        fti = queryUtility(IDexterityFTI, name='Issue Source')
        schema = fti.lookupSchema()
        self.assertEqual(IIssueSource, schema)

    def test_ct_issue_source_fti(self):
        fti = queryUtility(IDexterityFTI, name='Issue Source')
        self.assertTrue(fti)

    def test_ct_issue_source_factory(self):
        fti = queryUtility(IDexterityFTI, name='Issue Source')
        factory = fti.factory
        obj = createObject(factory)

        self.assertTrue(
            IIssueSource.providedBy(obj),
            u'IIssueSource not provided by {0}!'.format(
                obj,
            ),
        )

    def test_ct_issue_source_adding(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        obj = api.content.create(
            container=self.parent,
            type='Issue Source',
            id='issue_source',
        )

        self.assertTrue(
            IIssueSource.providedBy(obj),
            u'IIssueSource not provided by {0}!'.format(
                obj.id,
            ),
        )

        parent = obj.__parent__
        self.assertIn('issue_source', parent.objectIds())

        # check that deleting the object works too
        api.content.delete(obj=obj)
        self.assertNotIn('issue_source', parent.objectIds())

    def test_ct_issue_source_globally_not_addable(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        fti = queryUtility(IDexterityFTI, name='Issue Source')
        self.assertFalse(
            fti.global_allow,
            u'{0} is globally addable!'.format(fti.id)
        )

    def test_ct_issue_source_filter_content_type_true(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        fti = queryUtility(IDexterityFTI, name='Issue Source')
        portal_types = self.portal.portal_types
        parent_id = portal_types.constructContent(
            fti.id,
            self.portal,
            'issue_source_id',
            title='Issue Source container',
         )
        self.parent = self.portal[parent_id]
        with self.assertRaises(InvalidParameterError):
            api.content.create(
                container=self.parent,
                type='Document',
                title='My Content',
            )
