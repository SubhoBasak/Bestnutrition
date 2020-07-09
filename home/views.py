from django.shortcuts import render, redirect, reverse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views
from django.contrib.auth import login
from django.contrib import messages
from django.core.paginator import Paginator
from django.core.mail import send_mail
from django.utils import timezone
# from .ccavutil import encrypt, decrypt
from . import forms
from . import models
import datetime
import random

SERVER_EMAIL = 'subhobasak22@gmail.com'

merchant_id = '128690'
accessCode = 'AVBS69EC92CG63SBGC'
workingKey = 'EA984FDEACB61E2D131B5F64A52873DC'
currency = 'INR'
redirect_url = ''
cancel_url = ''
language = 'EN'
billing_country = 'India'


def index_view(request):
    return render(request, 'index.html')


def signup_view(request):
    status = 0
    form = forms.UserForm(request.POST)
    if form.is_valid():
        obj = form.save(commit=False)
        try:
            tmp = User.objects.get(email = obj.email)
            status = -1
        except User.DoesNotExist:
            obj.username = obj.email
            obj.set_password(obj.password)
            obj.save()
            login(request, obj)
            return redirect(reverse('index'))
    return render(request, 'signup.html', {'form': form, 'status': status})


class SigninView(auth_views.LoginView):
    template_name = 'signin.html'


class SignoutView(auth_views.LogoutView):
    template_name = 'signout.html'


def all_products(request):
    prod_s = models.Product.objects.all()
    page_s = Paginator(prod_s, 9)
    prod_s = page_s.get_page(request.GET.get('page'))
    return render(request, 'all-products.html', {'prod_s': prod_s})


def details_view(request, prod_id):
    try:
        main_prod = models.Product.objects.get(id=prod_id)
    except models.Product.DoesNotExist:
        return redirect(reverse('index'))
    if 'add_to_cart' in request.POST:
        if not request.user.is_authenticated:
            return redirect('/signin/?next='+request.path)
        try:
            obj = models.Cart.objects.get(user = request.user, product = main_prod)
            obj.quantity += 1
        except models.Cart.DoesNotExist:
            obj = models.Cart(user = request.user, product = main_prod)
        obj.save()
        return redirect(reverse('cart'))
    elif 'buy_now' in request.POST:
        return redirect('/select_address/'+str(main_prod.id)+'/1/')
    elif 'ask_question' in request.POST:
        return redirect(reverse('ask_question', args = [prod_id]))
    img_s = models.ProductImages.objects.filter(prod__id = prod_id)
    rel_prod_s = models.RelatedProduct.objects.filter(prod__id = prod_id)
    return render(request, 'details.html', {'main_prod': main_prod, 'img_s': img_s, 'rel_prod_s': rel_prod_s})


def about_us(request):
    return render(request, 'about-us.html')


def contact_us(request):
    submit = 0
    if 'your_name' in request.POST and 'your_email' in request.POST and 'your_phone' in request.POST and 'your_message' in request.POST:
        obj = models.ContactUsComment(name = request.POST['your_name'],
                                      email = request.POST['your_email'],
                                      phone = request.POST['your_phone'],
                                      message = request.POST['your_message'])
        obj.save()
        submit = 1
    return render(request, 'contact-us.html', {'submit': submit})


def forgot_view(request):
    status = 0
    if 'email_id' in request.POST:
        try:
            user = User.objects.get(email = request.POST['email_id'])
            otp = random.randint(100000, 999999)
            while len(models.PasswordReset.objects.filter(otp=otp)) != 0:
                otp = random.randint(100000, 999999)
            obj = models.PasswordReset(user_id=user.id, otp=otp)
            obj.save()
            # todo, at the production time we have to change this link
            tmp_url = 'http://localhost:8000/reset_password/' + str(otp)
            send_mail('Email verification',
                      'Reset you your password using the following link :\n' + tmp_url,
                      SERVER_EMAIL, [user.email,])
            status = 1
        except User.DoesNotExist:
            status = -1
    return render(request, 'forgot.html', {'status': status})


def reset_password_view(request, otp):
    status = 0
    try:
        obj = models.PasswordReset.objects.get(otp = otp)
        try:
            user = User.objects.get(username=obj.user.username)
            pswrd = str(random.randint(10000000, 99999999))
            user.set_password(pswrd)
            user.save()
            send_mail('New password',
                      'Your new login id is -\nUsername : ' + user.username + '\nPassword : ' + pswrd,
                      SERVER_EMAIL, [user.email])
            status = 1
            obj.delete()
        except User.DoesNotExist:
            status = -1
    except models.PasswordReset.DoesNotExist:
        status = -2
    return render(request, 'signin.html', {'status': status})


@login_required
def cart_view(request):
    cart_items = models.Cart.objects.filter(user=request.user)
    wish_list_items = models.WishList.objects.filter(user = request.user)
    if 'check_out' in request.POST:
        return redirect('/select_address/0/2/')
    elif 'remove_item_cart' in request.POST:
        try:
            obj = cart_items.get(id = request.POST['remove_item_cart'])
            obj.delete()
        except Exception as e:
            pass
    elif 'save_for_later' in request.POST:
        try:
            cart_obj = cart_items.get(id = request.POST['save_for_later'])
            wish_list_obj = models.WishList(user = request.user, product = cart_obj.product, quantity = cart_obj.quantity)
            wish_list_obj.save()
            cart_obj.delete()
        except Exception as e:
            pass
    elif 'move_to_cart' in request.POST:
        try:
            wish_list_obj = wish_list_items.get(id = request.POST['move_to_cart'])
            cart_obj = models.Cart(user = request.user, product = wish_list_obj.product, quantity = wish_list_obj.quantity)
            cart_obj.save()
            wish_list_obj.delete()
        except Exception as e:
            pass
    elif 'remove_item_wish_list' in request.POST:
        try:
            obj = wish_list_items.get(id = request.POST['remove_item_wish_list'])
            obj.delete()
        except Exception as e:
            pass
    elif 'change_qty' in request.POST and 'prod_id' in request.POST:
        try:
            obj = cart_items.get(id = request.POST['prod_id'])
            if request.POST['change_qty'] == '+':
                obj.quantity += 1
            elif request.POST['change_qty'] == '-':
                obj.quantity -= 1
            if obj.quantity == 0:
                obj.delete()
            else:
                obj.save()
        except Exception as e:
            pass

    total = 0
    quantity = 0
    delivery = 100
    for item in cart_items:
        total += item.product.price * item.quantity
        quantity += item.quantity
    if total > 1000 or quantity == 0:
        delivery = 0
    grand_total = total+delivery
    return render(request, 'cart.html',
                  {'cart_items': cart_items, 'cart_total': total, 'quantity': quantity,
                   'delivery': delivery, 'grand_total': grand_total, 'wish_list_items': wish_list_items,
                   })


def subscribe_newsletter(request):
    if 'new_email' in request.POST:
        if len(models.NewsLetterSubscriber.objects.filter(email = request.POST['new_email'])) == 0:
            uid = str(random.randint(1000000000, 9999999999))
            while len(models.NewsLetterSubscriber.objects.filter(uid = uid)) != 0:
                uid = uid = str(random.randint(1000000000, 9999999999))
            obj = models.NewsLetterSubscriber(email = request.POST['new_email'], uid = uid)
            obj.save()
            messages.success(request, 'Thank you for join our news letter.')
    return redirect(reverse('index'))


def unsubscribe_newsletter(request, uid):
    try:
        obj = models.NewsLetterSubscriber.objects.get(uid = uid)
        obj.delete()
        messages.success(request, 'You have unsubscribed our news letter.')
    except models.NewsLetterSubscriber.DoesNotExist:
        pass
    return redirect(reverse('index'))


# def track_order(request):
#     status = 0
#     if 'track_id' in request.GET:
#         try:
#             order = models.Order.objects.get(id = request.GET['track_id'])
#         except models.Order.DoesNotExist:
#             status = -1
#     return render(request, 'track_order.html', {'order': order, 'status': status})


@login_required
def ask_question_view(request, prod_id):
    submit = 0
    if 'your_name' in request.POST and 'your_email' in request.POST and 'your_subject' in request.POST and 'your_question' in request.POST:
        try:
            product = models.Product.objects.get(id = request.POST['product_id'])
        except Exception as e:
            messages.error(request, 'Product not found!')
            return redirect(reverse('index'))
        obj = models.Question(user = request.user,
                              product = product,
                              subject = request.POST['your_subject'],
                              question = request.POST['your_question'])
        obj.save()
        submit = 1
    return render(request, 'ask-question.html', {'product_id': prod_id, 'submit': submit})


@login_required
def select_address(request, prod_id, buy_type):
    try:
        cur_address = models.Address.objects.get(user = request.user)
    except models.Address.DoesNotExist:
        cur_address = models.Address(user = request.user)
        cur_address.save()
    form = forms.AddressForm(request.POST or None, instance = cur_address)
    if form.is_valid():
        cur_address = form.save(commit=False)
        cur_address.user = request.user
        cur_address.save()
        this_oid = 'ORDID'+timezone.now().strftime('%Y%m%d%H%M%S')+str(request.user.id)
        this_order = models.Order(user = request.user, oid = this_oid,
                                  first_name = cur_address.first_name,
                                  last_name = cur_address.last_name,
                                  address = cur_address.address,
                                  city = cur_address.city,
                                  state = cur_address.state,
                                  phone = cur_address.phone,
                                  pin_code = cur_address.pin_code)
        this_order.save()
        if buy_type == 1:
            try:
                main_prod = models.Product.objects.get(id=prod_id)
            except models.Product.DoesNotExist:
                return redirect(reverse('index'))
            prod_list = models.ProductList(product = main_prod, price = main_prod.price, quantity = 1, order = this_order)
            prod_list.save()
            this_order.total = main_prod.price
            this_order.save()
        elif buy_type == 2:
            cart_items = models.Cart.objects.filter(user = request.user)
            if len(cart_items) == 0:
                return redirect(reverse('index'))
            cur_total = 0
            for each_item in cart_items:
                prod_list = models.ProductList(product = each_item.product, price = each_item.product.price, quantity = each_item.quantity, order = this_order)
                prod_list.save()
                cur_total += each_item.product.price * each_item.quantity
            if cur_total < 1000:
                cur_total += 100
            this_order.total = cur_total
            this_order.save()
            cart_items.delete()

    return render(request, 'updateAddress.html', {'form': form})


def site_map(request):
    all_items = models.Product.objects.all()
    return render(request, 'site-mape.html', {'all_items': all_items})


def distributors(request):
    status = 0
    if 'name' in request.POST and 'email' in request.POST and 'subject' in request.POST and 'message' in request.POST:
        obj = models.Distributor(name=request.POST['name'],
                                 email=request.POST['email'],
                                 subject=request.POST['subject'],
                                 message=request.POST['message'])
        obj.save()
        status = 1
    return render(request, 'distributors.html', {'status': status})


@login_required
def profile(request):
    try:
        cur_user = User.objects.get(id = request.user.id)
    except User.DoesNotExist:
        return redirect(reverse('index'))
    try:
        address = models.Address.objects.get(user=request.user)
    except models.Address.DoesNotExist:
        address = models.Address()
        address.user = request.user
    if 'user_update' in request.POST:
        cur_user.first_name = request.POST['first_name']
        cur_user.last_name = request.POST['last_name']
        cur_user.save()
    elif 'address_update' in request.POST:
        address.first_name = request.POST['first_name']
        address.last_name = request.POST['last_name']
        address.phone = request.POST['phone']
        address.address = request.POST['address']
        address.city = request.POST['city']
        address.state = request.POST['state']
        address.pin_code = request.POST['pin_code']
        address.save()
    return render(request, 'profile.html', {'cur_user': cur_user, 'address': address})


@login_required
def checkout(request):
    pass


@login_required
def buy_now(request, pid):
    try:
        address = models.Address.objects.get(user = request.user)
    except models.Address.DoesNotExist:
        return redirect('/add_address/?next=buy_now/' + str(pid))
    new_order = models.Order(user=request.user, address=address.address, phone = address.phone,
                             city=address.city, state=address.state, pin_code=address.pin_code,
                             first_name=address.first_name, last_name=address.last_name)
    new_order.oid = 'ORDID'+timezone.now().strftime('%Y%m%d%H%M%S')+str(request.user.id)
    new_order.save()
    try:
        product = models.Product.objects.get(id = pid)
        product_list = models.ProductList()
        product_list.product = product
        product_list.quantity = 1
        product_list.price = product.price
        product_list.order = new_order
        product_list.save()
    except models.Product.DoesNotExist:
        return redirect(reverse('index'))
    total = product.price
    if total < 1000:
        total += 100
    new_order.total = total
    new_order.save()

    return redirect(reverse('my_orders'))


@login_required
def my_orders(request):
    if 'cancel_order' in request.POST:
        try:
            order = models.Order.objects.get(oid = request.POST['cancel_order'])
            order.status = '7'
            order.save()
        except models.Order.DoesNotExist:
            pass
    elif 'return_order' in request.POST:
        try:
            order = models.Order.objects.get(oid=request.POST['return_order'])
            order.status = '6'
            order.save()
        except models.Order.DoesNotExist:
            pass
    orders = models.Order.objects.filter(user = request.user)
    return render(request, 'orders.html', {'my_orders': orders})


@login_required
def review(request, pid):
    try:
        product = models.Product.objects.get(id = pid)
    except models.Product.DoesNotExist:
        return redirect(reverse('index'))
    if 'save_review' in request.POST:
        obj = models.Review(product = product)
        obj.user = request.user
        obj.rating = request.POST['rating']
        obj.text = request.POST['review_text']
        obj.save()
        return redirect(reverse('my_account'))
    return render(request, 'review.html')
