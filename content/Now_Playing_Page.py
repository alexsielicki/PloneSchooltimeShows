# -*- coding: utf-8 -*-
#
# File: Now_Playing_Page.py
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

from Products.ATContentTypes.content.document import ATDocument
from Products.ATContentTypes.content.document import ATDocumentSchema
from Products.PloneSchooltimeShows.config import *

##code-section module-header #fill in your manual code here
##/code-section module-header

schema = Schema((


),
)

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

Now_Playing_Page_schema = ATDocumentSchema.copy() + \
    schema.copy()

##code-section after-schema #fill in your manual code here
##/code-section after-schema

class Now_Playing_Page(ATDocument):
    """
    """
    security = ClassSecurityInfo()

    implements(interfaces.INow_Playing_Page)

    meta_type = 'Now_Playing_Page'
    _at_rename_after_creation = True

    schema = Now_Playing_Page_schema

    ##code-section class-header #fill in your manual code here
    ##/code-section class-header

    # Methods

registerType(Now_Playing_Page, PROJECTNAME)
# end of class Now_Playing_Page

##code-section module-footer #fill in your manual code here
##/code-section module-footer

