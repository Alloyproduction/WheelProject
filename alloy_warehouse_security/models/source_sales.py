# -*- coding: utf-8 -*-

from odoo import models, fields


class ResUser(models.Model):
    _inherit = "res.users"

    warehouse_id = fields.Many2one('stock.warehouse', 'Warehouse')
    project_id = fields.Many2one('project.project', 'Project')
