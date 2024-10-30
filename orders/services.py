

from decimal import Decimal
from django.db import transaction
from .models import Order, User, Cryptocurrency


class OrderService:
    _pending_orders = {}

    def create_order(self, user_id, cryptocurrency_name, amount):
        user = User.objects.get(id=user_id)
        crypto = Cryptocurrency.objects.get(name=cryptocurrency_name)

        cost = crypto.price * amount
        if user.balance < cost:
            raise ValueError("Insufficient balance.")

        with transaction.atomic():
            user.balance -= cost
            user.save()

            order = Order.objects.create(
                user=user,
                cryptocurrency=crypto,
                amount=amount,
                processed=False
            )

        self._add_to_pending_orders(crypto.name, amount)
        return order

    def _add_to_pending_orders(self, crypto_name, amount):
        if crypto_name not in self._pending_orders:
            self._pending_orders[crypto_name] = Decimal(0)
        self._pending_orders[crypto_name] += amount

        # If the total amount for this cryptocurrency is >= 10 USD, process it
        crypto = Cryptocurrency.objects.get(name=crypto_name)
        if self._pending_orders[crypto_name] * crypto.price >= 10:
            self.buy_from_exchange(crypto_name, self._pending_orders[crypto_name])
            self._pending_orders[crypto_name] = Decimal(0)

    def buy_from_exchange(self, crypto_name, total_amount):
        # Placeholder for the actual exchange buy request
        print(f"Buying {total_amount} of {crypto_name} from the exchange.")

        # Update orders as processed
        Order.objects.filter(cryptocurrency__name=crypto_name, processed=False).update(processed=True)
