# -*- coding: utf-8 -*-
from Products.Five import BrowserView

from collective.permalink.interfaces import IPermalinkProvider
from plone.memoize.view import memoize


class PermalinkUrlView(BrowserView):
    """View for showing permalink on Plone contents"""

    def __call__(self):
        return self.permalink

    @property
    @memoize
    def permalink(self):
        """Get the permalink info from the context"""
        try:
            return IPermalinkProvider(self.context).get_permalink()
        except TypeError:
            return None
