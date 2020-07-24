{
    "name": "PHS Base",
    "summary": """
        Pharmasimple custom settings""",
    "description": """
        - install all dependencies
        - add custom settings
    """,
    "author": "Michael Michot",
    "website": "http://www.pharmasimple.com",
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    "category": "specific_industry_applications",
    "version": "12.0.1.0.1",
    # any module necessary for this one to work correctly
    "depends": ["base",
                # shopinvader
                "shopinvader",
                "shopinvader_assortment",
                "shopinvader_delivery_carrier",
                "shopinvader_image",
                "shopinvader_payment",
                "shopinvader_payment_manual",
                "shopinvader_product_stock",
                "shopinvader_search_engine",
                "invader_payment",
                "invader_payment_manual",
                # contact
                "contacts",
                # inventory
                "stock",
                # purchase
                "purchase",
                # sale
                "sale",
                ],
    # always loaded
    "data": [],
    # only loaded in demonstration mode
    "demo": [],
}
