from django.test import SimpleTestCase
from django.urls import reverse, resolve
from catalog.views import payment_complete, CheckoutView, CouponView, add_to_cart, remove_from_cart


# Create your tests here.
class TestUrls(SimpleTestCase):

    def test_list_url_payment_complete_is_resolved(self):
        url = reverse('payment_complete')
        self.assertEqual(resolve(url).func, payment_complete)

    def test_list_url_add_to_cart_is_resolved(self):
        url = reverse('add_to_cart', args=['slug'])
        self.assertEqual(resolve(url).func, add_to_cart)

    def test_list_url_remove_from_cart_is_resolved(self):
        url = reverse('remove_from_cart', args=['slug'])
        self.assertEqual(resolve(url).func, remove_from_cart)

    def test_list_url_checkoutView_is_resolved(self):
        url = reverse('checkout')
        self.assertEqual(resolve(url).func.view_class, CheckoutView)

    def test_list_url_couponView_is_resolved(self):
        url = reverse('add_coupon')
        self.assertEqual(resolve(url).func.view_class, CouponView)
