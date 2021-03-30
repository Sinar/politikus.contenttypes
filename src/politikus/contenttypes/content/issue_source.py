# -*- coding: utf-8 -*-
from collective import dexteritytextindexer
from plone.app.textfield import RichText
from plone.app.vocabularies.catalog import CatalogSource
from plone.app.z3cform.widget import RelatedItemsFieldWidget
from plone.autoform import directives
from plone.dexterity.content import Container
from plone.namedfile import field as namedfile
from plone.supermodel import model
from politikus.contenttypes import _
from z3c.relationfield.schema import RelationChoice
from z3c.relationfield.schema import RelationList
# from plone.supermodel.directives import fieldset
# from z3c.form.browser.radio import RadioFieldWidget
from zope import schema
from zope.interface import implementer


class IIssueSource(model.Schema):
    """ Marker interface and Dexterity Python Schema for IssueSource
    """

    # Issue
    directives.widget('issue',
                      RelatedItemsFieldWidget,
                      pattern_options={
                        'mode': 'auto',
                        'favourites': [],
                        }
                      )

    issue = RelationChoice(
            title=u'Issue',
            source=CatalogSource(portal_type='Issue'),
            required=False,
            )

    # Directly implicated
    directives.widget('directly_implicated',
                      RelatedItemsFieldWidget,
                      pattern_options={
                        'mode': 'auto',
                        'favourites': [],
                        }
                      )

    directly_implicated = RelationList(
            title=_(u'Directly Implicated'),
            description=_(u'''
            Persons, Organizations or Memberships, directly charged,
            principle actor or making statement related to this issue.'''),
            default=[],
            value_type=RelationChoice(
                source=CatalogSource(portal_type=[
                    'Person',
                    'Organization',
                    'Membership'])
                ),
            required=False,
            )

    # Inirectly implicated
    directives.widget('indirectly_implicated',
                      RelatedItemsFieldWidget,
                      pattern_options={
                        'mode': 'auto',
                        'favourites': [],
                        }
                      )

    indirectly_implicated = RelationList(
            title=_(u'Indirectly Implicated'),
            description=_(u'''
            Persons, Organizations or Memberships, indirectly charged,
            secondary actor or refered to in statement related to
            this issue.'''),
            default=[],
            value_type=RelationChoice(
                source=CatalogSource(portal_type=[
                    'Person',
                    'Organization',
                    'Relationship',
                    'Membership'])
                ),
            required=False,
            )

    # Circumstantially implicated

    directives.widget('circumstantial_implicated',
                      RelatedItemsFieldWidget,
                      pattern_options={
                        'mode': 'auto',
                        'favourites': [],
                        }
                      )


    circumstantial_implicated = RelationList(
            title=_(u'Circumstantially Implicated'),
            description=_(u'''
            Persons, Organizations, Relationships or Memberships
            implicated in circumstantial manner for
            this issue.'''),
            default=[],
            value_type=RelationChoice(
                source=CatalogSource(portal_type=[
                    'Person',
                    'Organization',
                    'Relationship',
                    'Membership'])
                ),
            required=False,
            )

    # Disclosing
    directives.widget('disclosing',
                      RelatedItemsFieldWidget,
                      pattern_options={
                        'mode': 'auto',
                        'favourites': [],
                        }
                      )

    disclosing = RelationList(
            title=_(u'Disclosing'),
            description=_(u'''
            Parties disclosing this information individuals
            or organizations'''),
            default=[],
            value_type=RelationChoice(
                source=CatalogSource(portal_type=[
                    'Person',
                    'Organization', ]
                    )
                ),
            required=False,
            )

    dexteritytextindexer.searchable('author')
    author = schema.TextLine(
        title=_(u'Author, Organization or Website Name'),
        required=False,
        )

    url = schema.URI(
            title=_(u'Source Link'),
            required=False,
            )

    dexteritytextindexer.searchable('author')
    author = schema.TextLine(
        title=_(u'Author, Organization or Website Name'),
        required=False,
        )

    url = schema.URI(title=_(u'Source Link'),
                     required=False,)

    dexteritytextindexer.searchable('notes')
    notes = RichText(
         title=_(u'Text'),
         required=False
     )



    # If you want, you can load a xml model created TTW here
    # and customize it in Python:

    # model.load('issue_source.xml')

    # directives.widget(level=RadioFieldWidget)
    # level = schema.Choice(
    #     title=_(u'Sponsoring Level'),
    #     vocabulary=LevelVocabulary,
    #     required=True
    # )

    # text = RichText(
    #     title=_(u'Text'),
    #     required=False
    # )

    # url = schema.URI(
    #     title=_(u'Link'),
    #     required=False
    # )

    # fieldset('Images', fields=['logo', 'advertisement'])
    # logo = namedfile.NamedBlobImage(
    #     title=_(u'Logo'),
    #     required=False,
    # )

    # advertisement = namedfile.NamedBlobImage(
    #     title=_(u'Advertisement (Gold-sponsors and above)'),
    #     required=False,
    # )

    # directives.read_permission(notes='cmf.ManagePortal')
    # directives.write_permission(notes='cmf.ManagePortal')
    # notes = RichText(
    #     title=_(u'Secret Notes (only for site-admins)'),
    #     required=False
    # )


@implementer(IIssueSource)
class IssueSource(Container):
    """
    """
