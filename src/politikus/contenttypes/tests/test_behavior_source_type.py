# -*- coding: utf-8 -*-
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.behavior.interfaces import IBehavior
from politikus.contenttypes.behaviors.source_type import ISourceTypeMarker
from politikus.contenttypes.testing import POLITIKUS_CONTENTTYPES_INTEGRATION_TESTING  # noqa
from zope.component import getUtility

import unittest


class SourceTypeIntegrationTest(unittest.TestCase):

    layer = POLITIKUS_CONTENTTYPES_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])

    def test_behavior_source_type(self):
        behavior = getUtility(IBehavior, 'politikus.contenttypes.source_type')
        self.assertEqual(
            behavior.marker,
            ISourceTypeMarker,
        )
