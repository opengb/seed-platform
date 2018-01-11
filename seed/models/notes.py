# !/usr/bin/env python
# encoding: utf-8
"""
:copyright (c) 2014 - 2017, The Regents of the University of California, through Lawrence Berkeley National Laboratory (subject to receipt of any required approvals from the U.S. Department of Energy) and contributors. All rights reserved.  # NOQA
:author
"""

from django.contrib.postgres.fields import JSONField
from django.db import models
from django.utils.translation import ugettext_lazy as _

from seed.lib.superperms.orgs.models import Organization
from seed.models import (
    Property,
    TaxLot,
)
from seed.models.projects import Project
from seed.utils.generic import obj_to_dict
from seed.landing.models import SEEDUser as User


class Note(models.Model):
    # Audit Log types
    NOTE = 0
    LOG = 1

    NOTE_TYPES = (
        (NOTE, 'Note'),
        (LOG, 'Log'),
    )

    name = models.CharField(_('name'), max_length=Project.PROJECT_NAME_MAX_LENGTH)
    note_type = models.IntegerField(choices=NOTE_TYPES, default=NOTE, null=True)

    text = models.TextField()

    organization = models.ForeignKey(Organization, null=True, related_name='notes')
    user = models.ForeignKey(User, null=True, related_name='notes') # who added the note
    property = models.ForeignKey(Property, null=True, related_name='notes')
    taxlot = models.ForeignKey(TaxLot, null=True, related_name='notes')

    # in the near future track the changes to the Property records by storing the changes in JSON. Proposed format:
    # {
    #    "property_state": [ {
    #       "field": "address_line_1",
    #       "previous_value": "123 Main Street",
    #       "new_value": "742 Evergreen Terrace"
    #       },
    #       {}],
    #    "property: [ { ... } ],
    #    "tax_lot_state": [ { ... } ],
    # }
    #
    log_data = JSONField(default=dict, null=True)

    # Track when the entry was created and when it was updated
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    DEFAULT_LABELS = [
        "Residential",
        "Non-Residential",
        "Violation",
        "Compliant",
        "Missing Data",
        "Questionable Report",
        "Update Bldg Info",
        "Call",
        "Email",
        "High EUI",
        "Low EUI",
        "Exempted",
        "Extension",
        "Change of Ownership",
    ]

    class Meta:
        ordering = ['-created']
        index_together = [['organization', 'note_type']]

    def to_dict(self):
        return obj_to_dict(self)
