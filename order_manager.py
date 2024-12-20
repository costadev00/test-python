class OrderManager:
    def __init__(self):
        self.orders = []

    def add_order(self, order_id, customer_name, order_value):
        if not isinstance(order_id, int) or order_id <= 0:
            raise ValueError("order_id must be a positive integer")
        if not isinstance(customer_name, str) or not customer_name.strip():
            raise ValueError("customer_name must be a non-empty string")
        if not isinstance(order_value, (int, float)) or order_value <= 0:
            raise ValueError("order_value must be a positive number")
        
        self.orders.append({"order_id": order_id, "customer_name": customer_name, "order_value": order_value})

    def calculate_total(self):
        return sum(order["order_value"] for order in self.orders)

    def apply_discount(self, discount_percentage):
        if not isinstance(discount_percentage, (int, float)) or discount_percentage < 0 or discount_percentage > 100:
            raise ValueError("Discount percentage must be between 0 and 100")
        
        for order in self.orders:
            order["order_value"] -= order["order_value"] * (discount_percentage / 100)

    def find_order_by_id(self, order_id):
        for order in self.orders:
            if order["order_id"] == order_id:
                return order
        return None