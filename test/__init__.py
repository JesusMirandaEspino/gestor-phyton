import unittest
import database as db

class unittest_database(unittest.TestCase):

    def setup(self):
        db.Clientes.lista = [ 
            db.Cliente('151', 'bob', 'loquillo'),
            db.Cliente('152', 'cheeto', 'saltarin'),
            db.Cliente('153', 'gato', 'gato')
        ]