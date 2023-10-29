# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo.addons.account.models.chart_template import update_taxes_from_templates


def migrate(cr, version):
    # DO NOT DO SHIT
    return
    update_taxes_from_templates(cr, 'l10n_fr.l10n_fr_pcg_chart_template')
