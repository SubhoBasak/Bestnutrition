from django.db import models
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.template.defaultfilters import truncatechars
from django.utils import timezone
import datetime

SERVER_EMAIL = 'subhobasak@gmail.com'


class Product(models.Model):
    thumbnail = models.ImageField(upload_to = 'product_thumb/')
    name = models.CharField(max_length=200, null = False, blank=False)
    sub_name = models.TextField(null = False, blank=False)
    price = models.IntegerField(null = False)
    rating = models.IntegerField(null = False, default = 0)
    ingredients = models.TextField(null = True, blank = True)
    suggested = models.TextField(null = True, blank = True)
    packing = models.TextField(null = True, blank = True)
    reminder = models.TextField(null = True, blank = True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name',]


class RelatedProduct(models.Model):
    prod = models.ForeignKey(Product, on_delete = models.CASCADE)
    rel_prod = models.ForeignKey(Product, on_delete = models.CASCADE, related_name = 'rel_prod', related_query_name= 'rel_prod')


class ProductImages(models.Model):
    prod = models.ForeignKey(Product, on_delete = models.CASCADE)
    image = models.ImageField(upload_to= 'product_images/', null = False, blank = False)
    zoom = models.ImageField(upload_to= 'product_images_zoom/', null = False, blank= False)


class Address(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100, null=False, blank=False)
    last_name = models.CharField(max_length=100, null=False, blank=False)
    phone = models.CharField(max_length=15, null=False, blank=False)
    address = models.TextField(null=False, blank=False)
    city = models.CharField(max_length=200, null=False, blank=False)
    state = models.CharField(max_length=200, null=False, blank=False)
    pin_code = models.CharField(max_length=6, null=False, blank=False)


class BaseUserProduct(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    date_time = models.DateTimeField(auto_now_add=True, null=False)

    class Meta:
        abstract = True
        ordering = ['date_time']


class Review(BaseUserProduct):
    rating = models.CharField(max_length=1, null=False, default=5)
    review = models.TextField(null=True, blank=True)


class Question(BaseUserProduct):
    subject = models.CharField(max_length=200)
    question = models.TextField(null=False, blank=False)
    answer = models.TextField(null=False, blank=False)
    read = models.BooleanField(default=False)


class Order(models.Model):
    oid = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total = models.FloatField(default=0.0)
    payment_status = models.CharField(max_length=1, default='1', choices = [('1', 'Pending payment'), ('2', 'Payment done')])
    status = models.CharField(max_length=1, default='?',
                              choices=[('3', 'Packed'), ('4', 'Shipped'), ('5', 'Delivered'), ('6', 'Returned'), ('7', 'Canceld'), ('8', 'Refunded')])
    status_message = models.TextField(null=True, blank=True)
    order_date_time = models.DateTimeField(null=False, auto_now_add=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    address = models.TextField()
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    pin_code = models.CharField(max_length=6)

    @property
    def is_returnable(self):
        return self.order_date_time >= timezone.now() - datetime.timedelta(days = 7)

    class Meta:
        ordering = ('-order_date_time',)


class ProductList(models.Model):
    order = models.ForeignKey(Order, on_delete=models.PROTECT)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.FloatField(default=0.0)
    quantity = models.IntegerField(null=False)

    def __str__(self):
        return self.product.name


class BaseCartWishList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    class Meta:
        abstract = True


class Cart(BaseCartWishList):
    quantity = models.IntegerField(null=False, default=1)

    class Meta:
        ordering = ['product',]


class WishList(BaseCartWishList):
    quantity = models.IntegerField(null=False, default=1)

    class Meta:
        ordering = ['product',]


class PasswordReset(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    otp = models.IntegerField()


class NewsLetterSubscriber(models.Model):
    uid = models.CharField(max_length=10)
    email = models.EmailField()

    def __str__(self):
        return self.email


class EmailNews(models.Model):
    subject = models.CharField(max_length=200, null=False, blank=False)
    body = models.TextField(null=False, blank=False)
    date_time = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        for email in NewsLetterSubscriber.objects.all():
            send_mail(self.subject,
                  self.body+'\n\nUnsubscribe : http://localhost:8000/unsubscribe/'+email.uid,
                  SERVER_EMAIL, [email.email])

    def __str__(self):
        return self.subject


class ContactUsComment(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length = 15)
    message = models.TextField()
    date_time = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['date_time',]


class Distributor(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    date_time = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default=False)

    @property
    def short_message(self):
        return truncatechars(self.message, 50)

    class Meta:
        ordering = ['date_time',]