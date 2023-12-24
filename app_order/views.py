from datetime import datetime

from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from app_order.models import OrderItem, Order
from app_product.models import Product

class OrderCheckoutView(GenericAPIView):
    """
    Checkout for order
    """

    permission_classes = (
        IsAuthenticated,
    )

    def post(self, request):
        # Assuming product_ids and cart_detail are provided in the request or defined somewhere

        product_ids = request.data.get('product_ids', [])  # Assuming product_ids is passed in the request
        cart_detail = request.data.get('cart_detail', {})  # Assuming cart_detail is passed in the request

        if not product_ids:
            return Response({'message': 'No products provided for checkout.'}, status=status.HTTP_400_BAD_REQUEST)

        order = Order.objects.create(owner=request.user, pay_date=datetime.now())

        for product_id in product_ids:
            try:
                product = Product.confirmed.get(pk=product_id)
            except Product.DoesNotExist:
                return Response({'message': f'Product with ID {product_id} does not exist.'}, status=status.HTTP_404_NOT_FOUND)

            # Update product seller (assuming some modification is needed here)
            product.seller = request.user  # Assigning the seller as the current user

            # Save product changes
            product.save()

            OrderItem.objects.create(
                order=order,
                product=product,
                price=product.price,
                quantity=cart_detail.get(product_id, {}).get('quantity', 0),  # Accessing quantity from cart_detail
            )

        return Response({'message': 'Your cart has been paid successfully.'}, status=status.HTTP_200_OK)
