from decimal import Decimal
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .services import OrderService
from .models import User, Cryptocurrency


class BuyOrderAPIView(APIView):
    def post(self, request):
        user_id = request.data.get("user_id")
        crypto_name = request.data.get("crypto_name")
        amount = Decimal(request.data.get("amount"))

        try:
            order_service = OrderService()
            order = order_service.create_order(user_id, crypto_name, amount)
            return Response({"order_id": order.id, "status": "Order placed successfully"},
                            status=status.HTTP_201_CREATED)

        except User.DoesNotExist:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)

        except Cryptocurrency.DoesNotExist:
            return Response({"error": "Cryptocurrency not found"}, status=status.HTTP_404_NOT_FOUND)

        except ValueError as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
