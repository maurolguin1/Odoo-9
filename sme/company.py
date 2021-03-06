# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2009 Tiny SPRL (<http://tiny.be>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

import os

import openerp
import pytz
import time
from datetime import datetime
from openerp import SUPERUSER_ID, tools
from openerp.osv import fields, osv
from openerp.tools.translate import _
from openerp.tools.safe_eval import safe_eval as eval
from openerp.tools import image_resize_image
import openerp.addons.decimal_precision as dp

class sky_gaf(osv.osv):
    
  _inherit = "res.company"
  _name = 'res.company'

  _columns = { 
        'sky_gafver':fields.char('GAF Version', size=16, help="GST Audit File (GAF) Version Number"),
  }

  _defaults ={ }

sky_gaf()

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
