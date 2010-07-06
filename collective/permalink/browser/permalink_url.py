# -*- coding: utf-8 -*-

from Products.Five import BrowserView
from Products.CMFCore.utils import getToolByName

class PermalinkUrlView(BrowserView):
    """View for showing permalink on Archetype contents"""

    def __call__(self):
        context = self.context
        portal_url = getToolByName(context, 'portal_url')
        return portal_url()+'/resolveuid/%s' % context.UID()
    
    def hasPermalink(self):
        return True