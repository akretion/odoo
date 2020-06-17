from odoo.tests.common import TransactionCase, post_install
from odoo.exceptions import UserError, AccessError
from psycopg2 import IntegrityError


class HelloWorldTestCase(TransactionCase):
    """This class implements dummy unit tests for Hello World.
    """

    def setUp(self):
        super(HelloWorldTestCase, self).setUp()

    def test_create_product(self):
        """Simple Hello creation

        .. code-block:: python

           create with name toto -> check message = "Hello toto"
        """
        helloworld = self.env['phs.hello.world']

        r = helloworld.create({'name': 'toto'})
        self.assertEqual(r.message == 'Hello toto')
