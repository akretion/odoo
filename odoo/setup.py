from configparser import ConfigParser

from setuptools import setup

cfg = ConfigParser()
cfg.read("phs.cfg")


setup(
    version=cfg.get("phs", "series") + "." + cfg.get("phs", "version"),
    name="odoo-addons-phs",
    description="Pharmasimple Odoo Addons",
    setup_requires=["setuptools-odoo"],
    install_requires=[
        'click-odoo-contrib>=1.4.1',
    ],
    odoo_addons={"odoo_version_override": "12.0"},
)
