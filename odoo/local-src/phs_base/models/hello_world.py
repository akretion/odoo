from odoo import api, fields, models


class HelloWorld(models.Model):
    _name = "phs.hello.world"

    name = fields.Char()
    message = fields.Text()

    @api.model
    def create(self, values):

        return super(HelloWorld, self).create(values)
