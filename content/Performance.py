# -*- coding: utf-8 -*-
#
# File: Performance.py
#
# Copyright (c) 2012 by unknown <unknown>
# Generator: ArchGenXML Version 2.6
#            http://plone.org/products/archgenxml
#
# GNU General Public License (GPL)
#

__author__ = """unknown <unknown>"""
__docformat__ = 'plaintext'

from AccessControl import ClassSecurityInfo
from Products.Archetypes.atapi import *
from zope.interface import implements
import interfaces

from Products.CMFDynamicViewFTI.browserdefault import BrowserDefaultMixin

from Products.ATContentTypes.content.event import ATEvent
from Products.ATContentTypes.content.event import ATEventSchema
from Products.PloneSchooltimeShows.config import *

##code-section module-header #fill in your manual code here
##/code-section module-header

copied_fields = {}
copied_fields['location'] = ATEventSchema['location'].copy()
copied_fields['location'].widget.visible = 0
copied_fields['attendees'] = ATEventSchema['attendees'].copy()
copied_fields['attendees'].widget.visible = 0
copied_fields['eventUrl'] = ATEventSchema['eventUrl'].copy()
copied_fields['eventUrl'].widget.visible = ""
copied_fields['contactName'] = ATEventSchema['contactName'].copy()
copied_fields['contactName'].widget.visible = 0
copied_fields['contactEmail'] = ATEventSchema['contactEmail'].copy()
copied_fields['contactEmail'].widget.visible = 0
copied_fields['contactPhone'] = ATEventSchema['contactPhone'].copy()
copied_fields['contactPhone'].widget.visible = 0
# Alex Plone 4 Upgrade: eventType is gone in Plone 4, just using subject.
copied_fields['subject'] = ATEventSchema['subject'].copy()
#copied_fields['eventType'].schemata = 'categories'
schema = Schema((

    BooleanField(
        name='soldOut',
        widget=BooleanField._properties['widget'](
            label="Sold Out",
            description="Check this to indicate that this performance is sold out.",
            label_msgid='PloneSchooltimeShows_label_soldOut',
            description_msgid='PloneSchooltimeShows_help_soldOut',
            i18n_domain='PloneSchooltimeShows',
        ),
    ),

    # Alex adding new full field here without using ArgoUML or ArchGenXML because I don't have access to it.
    # Next time ArchGenXML is run it will strip out this new field, so it will need to be added through ArgoUML
    # in the long run. But due to time and budget constraints, I'm just adding it here manually for now.
    BooleanField(
        name='full',
        widget=BooleanField._properties['widget'](
            label="Full",
            description="Check this to indicate that this performance is full.",
        ),
    ),

    copied_fields['location'],

    copied_fields['attendees'],

    copied_fields['eventUrl'],

    copied_fields['contactName'],

    copied_fields['contactEmail'],

    copied_fields['contactPhone'],

    copied_fields['subject'],


),
)

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

Performance_schema = ATEventSchema.copy() + \
    schema.copy()

##code-section after-schema #fill in your manual code here
##/code-section after-schema

class Performance(ATEvent):
    """
    """
    security = ClassSecurityInfo()

    implements(interfaces.IPerformance)

    meta_type = 'Performance'
    _at_rename_after_creation = True

    schema = Performance_schema

    ##code-section class-header #fill in your manual code here
    ##/code-section class-header

    # Methods


registerType(Performance, PROJECTNAME)
# end of class Performance

##code-section module-footer #fill in your manual code here
##/code-section module-footer

