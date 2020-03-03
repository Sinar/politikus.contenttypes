# -*- coding: utf-8 -*-
from politikus.contenttypes.behaviors.procurement_categories import IProcurementCategoriesMarker
from politikus.contenttypes.testing import POLITIKUS_CONTENTTYPES_INTEGRATION_TESTING  # noqa
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.behavior.interfaces import IBehavior
from zope.component import getUtility

import unittest


class ProcurementCategoriesIntegrationTest(unittest.TestCase):

    layer = POLITIKUS_CONTENTTYPES_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])

    def test_behavior_procurement_categories(self):
        behavior = getUtility(IBehavior, 'politikus.contenttypes.procurement_categories')
        self.assertEqual(
            behavior.marker,
            IProcurementCategoriesMarker,
        )
