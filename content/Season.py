# -*- coding: utf-8 -*-
#
# File: Season.py
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

from Products.ATContentTypes.content.folder import ATFolder
from Products.ATContentTypes.content.folder import ATFolderSchema
from Products.ATContentTypes.content.document import ATDocument
from Products.ATContentTypes.content.document import ATDocumentSchema
from Products.PloneSchooltimeShows.config import *

##code-section module-header #fill in your manual code here
from DateTime import DateTime
##/code-section module-header

schema = Schema((

    DateTimeField(
        name='donorRenewalStartDate',
        widget=DateTimeField._properties['widget'](
            label="Donor Renewal Start Date",
            description="Date when donors can start renewing their subscription",
            label_msgid='PloneSchooltimeShows_label_donorRenewalStartDate',
            description_msgid='PloneSchooltimeShows_help_donorRenewalStartDate',
            i18n_domain='PloneSchooltimeShows',
        ),
    ),
    DateTimeField(
        name='donorRenewalEndDate',
        widget=DateTimeField._properties['widget'](
            label="Donor Renewal End Date",
            description="Date when donors can no longer renew their subscription",
            label_msgid='PloneSchooltimeShows_label_donorRenewalEndDate',
            description_msgid='PloneSchooltimeShows_help_donorRenewalEndDate',
            i18n_domain='PloneSchooltimeShows',
        ),
    ),
    DateTimeField(
        name='seasonRenewalStartDate',
        widget=DateTimeField._properties['widget'](
            label="Subscription Renewal Start Date",
            description="Date when subscribers can start renewing their season tickets",
            label_msgid='PloneSchooltimeShows_label_seasonRenewalStartDate',
            description_msgid='PloneSchooltimeShows_help_seasonRenewalStartDate',
            i18n_domain='PloneSchooltimeShows',
        ),
    ),
    DateTimeField(
        name='seasonRenewalEndDate',
        widget=DateTimeField._properties['widget'](
            label="Subscription Renewal End Date",
            description="Date when subscribers can no longer renew their season tickets",
            label_msgid='PloneSchooltimeShows_label_seasonRenewalEndDate',
            description_msgid='PloneSchooltimeShows_help_seasonRenewalEndDate',
            i18n_domain='PloneSchooltimeShows',
        ),
    ),
    DateTimeField(
        name='seasonNewStartDate',
        widget=DateTimeField._properties['widget'](
            label="New Subscription Start Date",
            description="Date when new subscribers can start purchasing season tickets",
            label_msgid='PloneSchooltimeShows_label_seasonNewStartDate',
            description_msgid='PloneSchooltimeShows_help_seasonNewStartDate',
            i18n_domain='PloneSchooltimeShows',
        ),
    ),
    DateTimeField(
        name='seasonNewEndDate',
        widget=DateTimeField._properties['widget'](
            label="New Subscription End Date",
            description="Date when new subscribers can no longer purchase season tickets",
            label_msgid='PloneSchooltimeShows_label_seasonNewEndDate',
            description_msgid='PloneSchooltimeShows_help_seasonNewEndDate',
            i18n_domain='PloneSchooltimeShows',
        ),
    ),
    DateTimeField(
        name='individualTixStartDate',
        widget=DateTimeField._properties['widget'](
            label="Individual Ticket Purchase Start Date",
            description="Date when visitors can start buying individual tickets.  You can override this general date by specifying an Individual Ticket Purchase Start Date for each show.",
            label_msgid='PloneSchooltimeShows_label_individualTixStartDate',
            description_msgid='PloneSchooltimeShows_help_individualTixStartDate',
            i18n_domain='PloneSchooltimeShows',
        ),
    ),
    ImageField(
        name='donorRenewalImage',
        widget=ImageField._properties['widget'](
            label="Donor Renewal Image",
            description="Link image for donor renewals",
            label_msgid='PloneSchooltimeShows_label_donorRenewalImage',
            description_msgid='PloneSchooltimeShows_help_donorRenewalImage',
            i18n_domain='PloneSchooltimeShows',
        ),
        storage=AttributeStorage(),
        max_size=(110,220),
    ),
    ImageField(
        name='seasonRenewalImage',
        widget=ImageField._properties['widget'](
            label="Subscription Renewal Image",
            description="Link image for subscription renewals",
            label_msgid='PloneSchooltimeShows_label_seasonRenewalImage',
            description_msgid='PloneSchooltimeShows_help_seasonRenewalImage',
            i18n_domain='PloneSchooltimeShows',
        ),
        storage=AttributeStorage(),
        max_size=(110,220),
    ),
    ImageField(
        name='seasonNewImage',
        widget=ImageField._properties['widget'](
            label="New Subscription Image",
            description="Link image for new subscriptions",
            label_msgid='PloneSchooltimeShows_label_seasonNewImage',
            description_msgid='PloneSchooltimeShows_help_seasonNewImage',
            i18n_domain='PloneSchooltimeShows',
        ),
        storage=AttributeStorage(),
        max_size=(110,220),
    ),
    ImageField(
        name='individualTixImage',
        widget=ImageField._properties['widget'](
            label="Individual Ticket Image",
            description="Link image for individual tickets",
            label_msgid='PloneSchooltimeShows_label_individualTixImage',
            description_msgid='PloneSchooltimeShows_help_individualTixImage',
            i18n_domain='PloneSchooltimeShows',
        ),
        storage=AttributeStorage(),
        max_size=(110,220),
    ),
    StringField(
        name='donorRenewalLinkText',
        widget=StringField._properties['widget'](
            label="Donor Renewal Link Text",
            description="Link text for donor renewals",
            size=60,
            label_msgid='PloneSchooltimeShows_label_donorRenewalLinkText',
            description_msgid='PloneSchooltimeShows_help_donorRenewalLinkText',
            i18n_domain='PloneSchooltimeShows',
        ),
    ),
    StringField(
        name='seasonRenewalLinkText',
        widget=StringField._properties['widget'](
            label="Subscription Renewal Link Text",
            description="Link text for subscription renewals",
            size=60,
            label_msgid='PloneSchooltimeShows_label_seasonRenewalLinkText',
            description_msgid='PloneSchooltimeShows_help_seasonRenewalLinkText',
            i18n_domain='PloneSchooltimeShows',
        ),
    ),
    StringField(
        name='seasonNewLinkText',
        widget=StringField._properties['widget'](
            label="New Subscription Link Text",
            description="Link text for new subscriptions",
            size=60,
            label_msgid='PloneSchooltimeShows_label_seasonNewLinkText',
            description_msgid='PloneSchooltimeShows_help_seasonNewLinkText',
            i18n_domain='PloneSchooltimeShows',
        ),
    ),
    StringField(
        name='individualTixLinkText',
        widget=StringField._properties['widget'](
            label="Individual Ticket Link Text",
            description="Link text for individual ticket purchases",
            size=60,
            label_msgid='PloneSchooltimeShows_label_individualTixLinkText',
            description_msgid='PloneSchooltimeShows_help_individualTixLinkText',
            i18n_domain='PloneSchooltimeShows',
        ),
    ),
    StringField(
        name='donorRenewalLink',
        widget=StringField._properties['widget'](
            label="Donor Renewal Link URL",
            description="Link address for donor renewals",
            size=60,
            label_msgid='PloneSchooltimeShows_label_donorRenewalLink',
            description_msgid='PloneSchooltimeShows_help_donorRenewalLink',
            i18n_domain='PloneSchooltimeShows',
        ),
    ),
    StringField(
        name='seasonRenewalLink',
        widget=StringField._properties['widget'](
            label="Subscription Renewal Link URL",
            description="Link address for subscription renewals",
            size=60,
            label_msgid='PloneSchooltimeShows_label_seasonRenewalLink',
            description_msgid='PloneSchooltimeShows_help_seasonRenewalLink',
            i18n_domain='PloneSchooltimeShows',
        ),
    ),
    StringField(
        name='seasonNewLink',
        widget=StringField._properties['widget'](
            label="New Subscription Link URL",
            description="Link address for new subscriptions",
            size=60,
            label_msgid='PloneSchooltimeShows_label_seasonNewLink',
            description_msgid='PloneSchooltimeShows_help_seasonNewLink',
            i18n_domain='PloneSchooltimeShows',
        ),
    ),

),
)

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

Season_schema = ATFolderSchema + ATDocumentSchema.copy() + \
    schema.copy()

##code-section after-schema #fill in your manual code here
##/code-section after-schema

class Season(ATFolder, ATDocument):
    """
    """
    security = ClassSecurityInfo()

    implements(interfaces.ISeason)

    meta_type = 'Season'
    _at_rename_after_creation = True

    schema = Season_schema

    ##code-section class-header #fill in your manual code here
    ##/code-section class-header

    # Methods

    security.declarePublic('getLinkText')
    def getLinkText(self):
        """ Returns the appropriate Link Text based on date
        """
        linkText = ""
        now = DateTime()
        if now > self.getDonorRenewalStartDate():
            linkText = self.getDonorRenewalLinkText()
        if now > self.getSeasonRenewalStartDate():
            linkText = self.getSeasonRenewalLinkText()
        if now > self.getSeasonNewStartDate():
            linkText = self.getSeasonNewLinkText()
        if now > self.getIndividualTixStartDate():
            linkText = self.getIndividualTixLinkText()
        return linkText

    security.declarePublic('getLink')
    def getLink(self):
        """ Returns the appropriate Link based on date
        """
        link=""
        now = DateTime()
        if now > self.getDonorRenewalStartDate():
            link = self.getDonorRenewalLink()
        if now > self.getSeasonRenewalStartDate():
            link = self.getSeasonRenewalLink()
        if now > self.getSeasonNewStartDate():
            link = self.getSeasonNewLink()
        if now > self.getIndividualTixStartDate():
            link = None
        return link

    security.declarePublic('getSeasonImage')
    def getSeasonImage(self, scale=None):
        """ Returns the appropriate Image based on date
        """
        image=None
        now = DateTime()
        if now > self.getDonorRenewalStartDate():
            image = self.getDonorRenewalImage(scale='small')
        if now > self.getSeasonRenewalStartDate():
            image = self.getSeasonRenewalImage(scale='small')
        if now > self.getSeasonNewStartDate():
            image = self.getSeasonNewImage(scale='small')
        if now > self.getIndividualTixStartDate():
            image = self.getIndividualTixImage(scale='small')
        return image

    security.declarePublic('donorRenewalActive')
    def donorRenewalActive(self):
        """ Returns whether the donor renewal period is currently active
        """
        return self.isPeriodActive(self.getDonorRenewalStartDate(),
                                   self.getDonorRenewalEndDate(),
                                   alternateEndDate=self.getSeasonRenewalStartDate())

    security.declarePublic('seasonRenewalActive')
    def seasonRenewalActive(self):
        """ Returns whether the season renewal period is currently active
        """
        return self.isPeriodActive(self.getSeasonRenewalStartDate(),
                                   self.getSeasonRenewalEndDate(),
                                   alternateEndDate=self.getSeasonNewStartDate())

    security.declarePublic('seasonNewActive')
    def seasonNewActive(self):
        """ Returns whether the season new period is currently active
        """
        return self.isPeriodActive(self.getSeasonNewStartDate(),
                                   self.getSeasonNewEndDate(),
                                   alternateEndDate=self.getIndividualTixStartDate())

    security.declarePublic('individualTixActive')
    def individualTixActive(self):
        """ Returns whether the individual ticket period is currently active
        """
        active = False
        now = DateTime()
        startDate = self.getIndividualTixStartDate()
        if startDate and (now > startDate):
            active = True
        return active

    security.declarePublic('isPeriodActive')
    def isPeriodActive(self, startDate, endDate, alternateEndDate=None):
        """ Returns whether right now is between startDate and endDate or an alternateEndDate
        """
        active = False
        now = DateTime()
        if not endDate and alternateEndDate: #if there is no donor renewal end date
            endDate = alternateEndDate #set the end date to be the season renewal end date
        if startDate and endDate:
            if endDate > now > startDate:
                active = True
        return active


registerType(Season, PROJECTNAME)
# end of class Season

##code-section module-footer #fill in your manual code here
##/code-section module-footer

