# -*- coding: utf-8 -*-

from zope.interface import Interface

##code-section HEAD
##/code-section HEAD

class ISeason(Interface):
    """Marker interface for .Season.Season
    """

class IShow(Interface):
    """Marker interface for .Show.Show
    """

class IPerformance(Interface):
    """Marker interface for .Performance.Performance
    """

class INow_Playing_Page(Interface):
    """Marker interface for .Now_Playing_Page.Now_Playing_Page
    """

##code-section FOOT
##/code-section FOOT