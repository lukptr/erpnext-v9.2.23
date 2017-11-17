# -*- coding: utf-8 -*-
# Copyright (c) 2017, Frappe Technologies Pvt. Ltd. and Contributors
# See license.txt
from __future__ import unicode_literals

import frappe
import unittest

class TestSoilTexture(unittest.TestCase):
	def test_texture_selection(self):
		sample_texture = {
			'doctype': 'Soil Texture',
			'geolocation': '{"type":"FeatureCollection","features":[{"type":"Feature","properties":{},"geometry":{"type":"Point","coordinates":[72.882185,19.076395]}}]}',
			'date': '2017-11-08',
			'clay_composition': 20,
			'sand_composition': 30
		}

		doc = frappe.get_doc(sample_texture)
		doc.save()

		soil_tex = frappe.get_doc('Soil Texture', doc.name)
		self.assertEquals(soil_tex.silt_composition, 50)
		self.assertEquals(soil_tex.soil_type, 'Silt Loam')