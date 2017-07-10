# -*- coding: utf-8 -*-
# Copyright (c) 2017, frappe and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _
from frappe.model.document import Document

class Meeting(Document):
	def validate(self):
		""" Set missing names and avoid duplication """
		for attendee in self.attendees:
			if not attendee.full_name:
				attendee.full_name = get_full_name(attendee.attendee)

@frappe.whitelist()
def get_full_name(attendee):
	""" Fetch the full name of the User from 'User Doctype' """
	user =  frappe.get_doc("User", attendee)
	# Filter and add First name / Last name
	return " ".join(filter(None, [user.first_name, user.middle_name, user.last_name]))