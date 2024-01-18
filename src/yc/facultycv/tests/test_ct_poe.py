# -*- coding: utf-8 -*-
from plone import api
from plone.api.exc import InvalidParameterError
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.dexterity.interfaces import IDexterityFTI
from yc.facultycv.content.poe import IPoe  # NOQA E501
from yc.facultycv.testing import YC_FACULTYCV_INTEGRATION_TESTING  # noqa
from zope.component import createObject
from zope.component import queryUtility

import unittest


class PoeIntegrationTest(unittest.TestCase):

    layer = YC_FACULTYCV_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        portal_types = self.portal.portal_types
        parent_id = portal_types.constructContent(
            'directory',
            self.portal,
            'parent_container',
            title='Parent container',
        )
        self.parent = self.portal[parent_id]

    def test_ct_poe_schema(self):
        fti = queryUtility(IDexterityFTI, name='poe')
        schema = fti.lookupSchema()
        self.assertEqual(IPoe, schema)

    def test_ct_poe_fti(self):
        fti = queryUtility(IDexterityFTI, name='poe')
        self.assertTrue(fti)

    def test_ct_poe_factory(self):
        fti = queryUtility(IDexterityFTI, name='poe')
        factory = fti.factory
        obj = createObject(factory)

        self.assertTrue(
            IPoe.providedBy(obj),
            u'IPoe not provided by {0}!'.format(
                obj,
            ),
        )

    def test_ct_poe_adding(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        obj = api.content.create(
            container=self.parent,
            type='poe',
            id='poe',
        )

        self.assertTrue(
            IPoe.providedBy(obj),
            u'IPoe not provided by {0}!'.format(
                obj.id,
            ),
        )

        parent = obj.__parent__
        self.assertIn('poe', parent.objectIds())

        # check that deleting the object works too
        api.content.delete(obj=obj)
        self.assertNotIn('poe', parent.objectIds())

    def test_ct_poe_globally_not_addable(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        fti = queryUtility(IDexterityFTI, name='poe')
        self.assertFalse(
            fti.global_allow,
            u'{0} is globally addable!'.format(fti.id)
        )

    def test_ct_poe_filter_content_type_true(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        fti = queryUtility(IDexterityFTI, name='poe')
        portal_types = self.portal.portal_types
        parent_id = portal_types.constructContent(
            fti.id,
            self.portal,
            'poe_id',
            title='poe container',
        )
        self.parent = self.portal[parent_id]
        with self.assertRaises(InvalidParameterError):
            api.content.create(
                container=self.parent,
                type='Document',
                title='My Content',
            )
