# -*- coding: utf-8 -*-
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from yc.facultycv.testing import YC_FACULTYCV_FUNCTIONAL_TESTING
from yc.facultycv.testing import YC_FACULTYCV_INTEGRATION_TESTING
from zope.component import getMultiAdapter
from zope.component.interfaces import ComponentLookupError

import unittest


class ViewsIntegrationTest(unittest.TestCase):

    layer = YC_FACULTYCV_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        api.content.create(self.portal, 'Folder', 'other-folder')
        api.content.create(self.portal, 'Document', 'front-page')

    def test_cvvoltomigration_is_registered(self):
        view = getMultiAdapter(
            (self.portal['other-folder'], self.portal.REQUEST),
            name='cvvoltomigration'
        )
        self.assertTrue(view.__name__ == 'cvvoltomigration')
        # self.assertTrue(
        #     'Sample View' in view(),
        #     'Sample View is not found in cvvoltomigration'
        # )

    def test_cvvoltomigration_not_matching_interface(self):
        with self.assertRaises(ComponentLookupError):
            getMultiAdapter(
                (self.portal['front-page'], self.portal.REQUEST),
                name='cvvoltomigration'
            )


class ViewsFunctionalTest(unittest.TestCase):

    layer = YC_FACULTYCV_FUNCTIONAL_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
