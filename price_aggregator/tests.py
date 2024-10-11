from django.test import TestCase
from django.urls import reverse
from .models import Product
from decimal import Decimal
from price_aggregator.helpers.scraper import amazon_list



# Test case for Product model and views


class ProductModelTest(TestCase):

    # Set up test data for the Product model
    @classmethod
    def setUp(self):
        self.product = Product.objects.create(
            name='Test Product',
            price=Decimal('29.99'),
            description='This is a test product'
        )

    # Test the string representation of the Product model
    def test_product_str(self):
        self.assertEqual(str(self.product), 'Test Product')

    # Test that the product was created correctly
    def test_product_creation(self):
        product = Product.objects.create(
            name='Test Product', price=Decimal('29.99'))
        self.assertEqual(product.price, Decimal('29.99'))

# Test case for Product views


class ProductViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Creating sample products for testing
        cls.product1 = Product.objects.create(
            name='Product 1',
            price=29.99,
            description="This is the first product")
        cls.product2 = Product.objects.create(
            name='Product 2',
            price=39.99,
            description="This is the second product")

    def test_product_list_view(self):
        # Test the product list view
        response = self.client.get(reverse('product_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'product_list.html')
        self.assertContains(response, 'Product 1')
        self.assertContains(response, 'Product 2')
        self.assertQuerysetEqual(
            response.context['products'].order_by('id'),  # Order the queryset
            # List of expected products
            [self.product1, self.product2],
            transform=lambda x: x
            # Transform to compare actual object instances, not repr strings
        )

    def test_product_detail_view(self):
        # Test the product detail view
        response = self.client.get(
            reverse(
                'product_detail', args=[
                    self.product1.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'product_detail.html')
        self.assertContains(response, 'Product 1')
        self.assertEqual(response.context['product'], self.product1)

        # Test with a non-existent product ID
        response = self.client.get(
            reverse(
                'product_detail',
                args=[10]))  # Assuming 10 does not exist
        self.assertEqual(response.status_code, 404)
        
#Testing the scraper
#amazon_list("Samsung galaxy S23 phone")
