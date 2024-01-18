# -*- coding: utf-8 -*-
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import yc.facultycv


class YcFacultycvLayer(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        import plone.app.dexterity
        self.loadZCML(package=plone.app.dexterity)
        import plone.restapi
        self.loadZCML(package=plone.restapi)
        self.loadZCML(package=yc.facultycv)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'yc.facultycv:default')


YC_FACULTYCV_FIXTURE = YcFacultycvLayer()


YC_FACULTYCV_INTEGRATION_TESTING = IntegrationTesting(
    bases=(YC_FACULTYCV_FIXTURE,),
    name='YcFacultycvLayer:IntegrationTesting',
)


YC_FACULTYCV_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(YC_FACULTYCV_FIXTURE,),
    name='YcFacultycvLayer:FunctionalTesting',
)


YC_FACULTYCV_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        YC_FACULTYCV_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE,
    ),
    name='YcFacultycvLayer:AcceptanceTesting',
)
