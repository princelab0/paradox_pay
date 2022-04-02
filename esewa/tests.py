from unicodedata import name
from django.test import TestCase
from django.urls import reverse

# Create your tests here.
from django.contrib.auth.models import Group
from .models import Product,Subscription,Transaction,UserSubscription

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



class TransactionModelTest(TestCase):
    def setUp(self):
        Transaction.objects.create(comment="test")

    def test_comment_content(self):
        transaction = Transaction.objects.get(id=1)
        expected_object_name = f'{transaction.comment}'
        self.assertEqual(expected_object_name,'test')

# class UserSubscriptionModelTest(TestCase):
#     def setUp(self):
#         UserSubscription.objects.create(expires='2022-10-28')

#     def test_expires_content(self):
#         usersub= UserSubscription.objects.get(id=1)
#         expected_object_name = {usersub.expires}
#         self.assertEqual(expected_object_name,'2022-10-28')
        


class HomePageViewTest(TestCase):
    def setUp(self):
        Product.objects.create(title='this is another test',price=20,image='media/products/abx.jpg')
    def test_view_url_exists_at_proper_location(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_by_name(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)
    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'home.html')

