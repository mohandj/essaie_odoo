# -*- coding: utf-8 -*-

 from odoo import models, fields, api


class devoir(models.Model):
    _inherit = 'sale.order'
    def action_encours(self):
        self.write({'state': 'encours'})


