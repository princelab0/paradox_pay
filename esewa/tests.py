from unicodedata import name
from django.test import TestCase

# Create your tests here.
from django.contrib.auth.models import Group
from .models import Product,Subscription

class ProductModelTest(TestCase):
    def setUp(self):
        Product.objects.create(title='test',price=10)

    def test_title_content(self):
        product = Product.objects.get(id=1)
        expected_object_name = f'{product.title}'
        self.assertEqual(expected_object_name, 'test')

    def test_price_content(self):
        product = Product.objects.get(id=1)
        expected_object_name = f'{product.price}'
        self.assertEqual(expected_object_name, '10')


class SubscriptionModelTest(TestCase):
    def setUp(self):
        
        Subscription.objects.create(name='test',price=10.00,description='test',trial_period=0,trial_unit='days',recurrence_unit='months',recurrence_period=1,group=Group.objects.create(name='test'))

    def test_title_content(self):
        subscription = Subscription.objects.get(id=1)
        expected_object_name = f'{subscription.name}'
        self.assertEqual(expected_object_name, 'test')
    
    def test_price_content(self):
        subscription = Subscription.objects.get(id=1)
        expected_object_name = f'{subscription.price}'
        self.assertEqual(expected_object_name, '10.00')
    
    def test_description_content(self):
        subscription = Subscription.objects.get(id=1)
        expected_object_name = f'{subscription.description}'
        self.assertEqual(expected_object_name, 'test')

    def test_trial_period_content(self):
        subscription = Subscription.objects.get(id=1)
        expected_object_name = f'{subscription.trial_period}'
        self.assertEqual(expected_object_name, '0')

    def test_trial_unit_content(self):
        subscription = Subscription.objects.get(id=1)
        expected_object_name = f'{subscription.trial_unit}'
        self.assertEqual(expected_object_name, 'days')
    
    def test_recurring_period_content(self):
        subscription = Subscription.objects.get(id=1)
        expected_object_name = f'{subscription.recurrence_period}'
        self.assertEqual(expected_object_name, '1')
    
    def test_recurring_unit_content(self):
        subscription = Subscription.objects.get(id=1)
        expected_object_name = f'{subscription.recurrence_unit}'
        self.assertEqual(expected_object_name, 'months')

     

    # def test_recurring_count_content(self):
    #     subscription = Subscription.objects.get(id=1)
    #     expected_object_name = f'{subscription.recurrence_count}'
    #     self.assertEqual(expected_object_name, '1')

    # def test_recurring_end_date_content(self):
    #     subscription = Subscription.objects.get(id=1)
    #     expected_object_name = f'{subscription.recurrence_end_date}'
    #     self.assertEqual(expected_object_name, '2022-04-01')\


    def test_group_content(self):
        subscription = Subscription.objects.get(id=1)
        expected_object_name = f'{subscription.group}'
        self.assertEqual(expected_object_name, 'test')