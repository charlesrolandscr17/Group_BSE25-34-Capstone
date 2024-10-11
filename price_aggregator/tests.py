from django.test import TestCase
from django.urls import reverse
from .models import Product
from decimal import Decimal
#from price_aggregator.helpers.scraper import amazon_list



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

    def test_product_list_view_get(self):
        # Test the product list view for GET request
        response = self.client.get(reverse('product_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'product_list.html')
        self.assertContains(response, 'Product 1')
        self.assertContains(response, 'Product 2')
        
        # Ensure products are in the context
        self.assertQuerysetEqual(
            response.context['scraped_data'],  # Adjust this to match your context variable name
            [self.product1, self.product2],
            transform=lambda x: x
        )

    def test_product_list_view_post(self):
        # Test the product list view for POST request with a query
        response = self.client.post(reverse('product_list'), {'query': 'Product 1'})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'product_list.html')
        
        # Verify the scraped_data context variable contains expected products
        self.assertContains(response, 'Product 1')
        self.assertNotContains(response, 'Product 2')  # Depending on your search functionality
    
        # Assuming the amazon_list function returns the product data
        self.assertQuerysetEqual(
            response.context['scraped_data'],
            [self.product1],
            transform=lambda x: x
        )

    def test_product_list_view_post_no_query(self):
        # Test the product list view for POST request with no query
        response = self.client.post(reverse('product_list'), {'query': ''})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'product_list.html')
        
        # Ensure that no products are shown when no query is provided
        self.assertContains(response, 'No products found')  # Adjust this line based on your template logic
        self.assertQuerysetEqual(
            response.context['scraped_data'],
            [],  # No products should be present
            transform=lambda x: x
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
