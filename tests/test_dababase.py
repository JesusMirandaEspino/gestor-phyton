import unittest
import database as db


class unittest_database(unittest.TestCase):

    def setup(self):
        db.Clientes.lista = [
            db.Cliente('151', 'bob', 'loquillo'),
            db.Cliente('152', 'cheeto', 'saltarin'),
            db.Cliente('153', 'gato', 'gato')
        ]

    def test_busacar_cliente(self):
        cliente_existe = db.Clientes.buscar('151')
        cliente_inexistente = db.Clientes.buscar('150')

        self.assertIsNotNone(cliente_existe)
        self.assertIsNone(cliente_inexistente)

    def test_crear_cliente(self):
        nuevo_cliente = db.Clientes.crear('39X', 'Héctor', 'Costa')

        self.assertEqual(len(db.Clientes.lista), 4)
        self.assertEqual(nuevo_cliente.dni, '39X')
        self.assertEqual(nuevo_cliente.nombre, 'Héctor')
        self.assertEqual(nuevo_cliente.apellido, 'Costa')

