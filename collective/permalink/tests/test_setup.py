# -*- coding: utf-8 -*-
"""Setup tests for this package."""
import unittest2 as unittest

from zope.component import getUtility
from zope.schema.interfaces import IVocabularyFactory

from collective.permalink.interfaces import IThemeSpecific
from collective.permalink.testing import \
    COLLECTIVE_PERMALINK_INTEGRATION_TESTING
from plone import api
from plone.browserlayer import utils


class TestSetup(unittest.TestCase):
    """Test that collective.permalink is properly installed."""

    layer = COLLECTIVE_PERMALINK_INTEGRATION_TESTING

    def setUp(self):  # noqa
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if collective.permalink is installed."""
        self.assertTrue(
            self.installer.isProductInstalled(
                'collective.permalink',
            ),
        )

    def test_browserlayer(self):
        """Test that IAddOnInstalled is registered."""
        self.assertIn(
            IThemeSpecific,
            utils.registered_layers(),
        )

    def test_behavior_available(self):
        """Test if Organizational Units Vocabulary is available."""
        voc = getUtility(
            IVocabularyFactory,
            'akbild.vocabularies.OrganizationalUnits',
        )
        self.assertTrue(bool(voc))


class TestUninstall(unittest.TestCase):
    """Uninstall Routine."""

    layer = COLLECTIVE_PERMALINK_INTEGRATION_TESTING

    def setUp(self):  # noqa
        """Setting up Testcase."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        self.installer.uninstallProducts(['collective.permalink'])

    def test_product_uninstalled(self):
        """Test if collective.permalink is cleanly uninstalled."""
        self.assertFalse(
            self.installer.isProductInstalled(
                'collective.permalink',
            ),
        )

    def test_browserlayer(self):
        """Test that IAddOnInstalled is removed."""
        self.assertNotIn(
            IThemeSpecific,
            utils.registered_layers(),
        )
