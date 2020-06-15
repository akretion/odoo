{
    "name": "Hello world",
    "summary": """
        Hello world dummy module use to illustrate the odoo_base project""",
    "description": """
        use as kind of documentation to illustrate how to add module
        and how to reference it in the requirements.txt.in
    """,
    "author": "Michael Michot",
    "website": "http://www.tuxmike.ovh",
    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    "category": "Uncategorized",
    "version": "12.0.1.0.1",
    # any module necessary for this one to work correctly
    "depends": ["base"],
    # always loaded
    "data": ["security/ir.model.access.csv", "views/hello_world.xml",],
    # only loaded in demonstration mode
    "demo": ["demo/demo.xml",],
}
