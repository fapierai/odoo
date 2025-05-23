# -*- coding: utf-8 -*-

from odoo import models, fields, api


class MyModule(models.Model):
    _name = 'my_module.model'
    _description = 'My Module Model'

    name = fields.Char(string='Name', required=True)
    description = fields.Text(string='Description')
    active = fields.Boolean(string='Active', default=True)
    
    # Add your fields here
    
    @api.model
    def create(self, vals):
        # Add your logic here
        return super(MyModule, self).create(vals)
    
    def write(self, vals):
        # Add your logic here
        return super(MyModule, self).write(vals)
