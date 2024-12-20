import unittest
from order_manager import OrderManager

class TestOrderManager(unittest.TestCase):
    
    def setUp(self):
        self.order_manager = OrderManager()

    def test_add_order(self):
        # Teste de adição de pedido válido
        self.order_manager.add_order(1, "John Doe", 100.0)
        self.assertEqual(self.order_manager.find_order_by_id(1), {"order_id": 1, "customer_name": "John Doe", "order_value": 100.0})

        # Teste com order_id inválido
        with self.assertRaises(ValueError):
            self.order_manager.add_order(0, "John Doe", 100.0)

        # Teste com customer_name inválido (vazio)
        with self.assertRaises(ValueError):
            self.order_manager.add_order(2, "", 100.0)

        # Teste com customer_name inválido (nulo)
        with self.assertRaises(ValueError):
            self.order_manager.add_order(2, None, 100.0)

        # Teste com order_value inválido
        with self.assertRaises(ValueError):
            self.order_manager.add_order(3, "Jane Doe", 0.0)

    def test_calculate_total(self):
        # Teste com vários pedidos
        self.order_manager.add_order(1, "John Doe", 100.0)
        self.order_manager.add_order(2, "Jane Doe", 200.0)
        self.assertEqual(self.order_manager.calculate_total(), 300.0)

        # Teste com nenhum pedido
        self.assertEqual(OrderManager().calculate_total(), 0.0)

    def test_apply_discount(self):
        # Teste com desconto de 10%
        self.order_manager.add_order(1, "John Doe", 100.0)
        self.order_manager.apply_discount(10)
        self.assertEqual(self.order_manager.find_order_by_id(1), {"order_id": 1, "customer_name": "John Doe", "order_value": 90.0})

        # Teste com desconto de 0%
        self.order_manager.apply_discount(0)
        self.assertEqual(self.order_manager.find_order_by_id(1), {"order_id": 1, "customer_name": "John Doe", "order_value": 90.0})

        # Teste com desconto inválido (maior que 100%)
        with self.assertRaises(ValueError):
            self.order_manager.apply_discount(105)

        # Teste com desconto inválido (negativo)
        with self.assertRaises(ValueError):
            self.order_manager.apply_discount(-10)

    def test_find_order_by_id(self):
        # Teste de pedido existente
        self.order_manager.add_order(1, "John Doe", 100.0)
        self.assertEqual(self.order_manager.find_order_by_id(1), {"order_id": 1, "customer_name": "John Doe", "order_value": 100.0})

        # Teste de pedido não existente
        self.assertIsNone(self.order_manager.find_order_by_id(2))

if __name__ == "__main__":
    unittest.main()