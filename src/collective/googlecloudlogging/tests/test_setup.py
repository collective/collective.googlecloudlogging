# -*- coding: utf-8 -*-
"""Setup tests for this package."""
import unittest

from plone import api
from plone.app.testing import TEST_USER_ID, setRoles

from collective.googlecloudlogging.testing import (  # noqa: E501
    COLLECTIVE_GOOGLECLOUDLOGGING_INTEGRATION_TESTING,
)

try:
    from Products.CMFPlone.utils import get_installer
except ImportError:
    get_installer = None


class TestSetup(unittest.TestCase):
    """Test that collective.googlecloudlogging is properly installed."""

    layer = COLLECTIVE_GOOGLECLOUDLOGGING_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        if get_installer:
            self.installer = get_installer(self.portal, self.layer['request'])
        else:
            self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if collective.googlecloudlogging is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'collective.googlecloudlogging'))

    def test_browserlayer(self):
        """Test that ICollectiveGooglecloudloggingLayer is registered."""
        from plone.browserlayer import utils

        from collective.googlecloudlogging.interfaces import (
            ICollectiveGooglecloudloggingLayer,
        )
        self.assertIn(
            ICollectiveGooglecloudloggingLayer,
            utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = COLLECTIVE_GOOGLECLOUDLOGGING_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        if get_installer:
            self.installer = get_installer(self.portal, self.layer['request'])
        else:
            self.installer = api.portal.get_tool('portal_quickinstaller')
        roles_before = api.user.get_roles(TEST_USER_ID)
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.installer.uninstallProducts(['collective.googlecloudlogging'])
        setRoles(self.portal, TEST_USER_ID, roles_before)

    def test_product_uninstalled(self):
        """Test if collective.googlecloudlogging is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'collective.googlecloudlogging'))

    def test_browserlayer_removed(self):
        """Test that ICollectiveGooglecloudloggingLayer is removed."""
        from plone.browserlayer import utils

        from collective.googlecloudlogging.interfaces import (
            ICollectiveGooglecloudloggingLayer,
        )
        self.assertNotIn(ICollectiveGooglecloudloggingLayer, utils.registered_layers())
