

from django.test import TestCase
from .models import User, Cryptocurrency, Order
from .services import OrderService


class OrderServiceTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create(username="test_user", balance=100)
        self.crypto = Cryptocurrency.objects.create(name="aban", price=4)
        self.service = OrderService()

    def test_create_order_success(self):
        order = self.service.create_order(self.user.id, "aban", 4)
        self.assertEqual(order.amount, 4)
        self.assertEqual(order.user.balance, 100 - (4 * 4))

    def test_insufficient_balance(self):
        self.user.balance = 5
        self.user.save()
        with self.assertRaises(ValueError):
            self.service.create_order(self.user.id, "aban", 2)
