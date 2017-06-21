# -*- coding: utf-8 -*-
from zope.interface import Interface

from plone.theme.interfaces import IDefaultPloneLayer


class IThemeSpecific(IDefaultPloneLayer):
    """Theme Layer Marker Interface."""


class IPermalinkProvider(Interface):
    """Interface for object that can provide Permalink data"""

    def get_permalink():
        """Obtain permalink"""
