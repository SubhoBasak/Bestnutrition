from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_view, name = 'index'),
    path('all_products/', views.all_products, name = 'all_products'),
    path('about_us/', views.about_us, name = 'about_us'),
    path('contact_us/', views.contact_us, name = 'contact_us'),
    path('details/<int:prod_id>/', views.details_view, name = 'details'),
    path('signin/', views.SigninView.as_view(), name = 'signin'),
    path('signup/', views.signup_view, name = 'signup'),
    path('signout/', views.SignoutView.as_view(), name = 'signout'),
    path('forgot/', views.forgot_view, name = 'forgot'),
    path('reset_password/<int:otp>/', views.reset_password_view, name = 'reset_password'),
    path('subscrible/', views.subscribe_newsletter, name = 'subscribe'),
    path('unsubscribe/<str:uid>/', views.unsubscribe_newsletter, name = 'unsubscribe'),
    path('ask_question/<int:prod_id>/', views.ask_question_view, name = 'ask_question'),
    path('cart/', views.cart_view, name = 'cart'),
    path('add_address/', views.add_address, name = 'add_address'),
    path('site_map/', views.site_map, name = 'site_map'),
    path('distributors/', views.distributors, name = 'distributors'),
    path('myaccount/', views.profile, name = 'my_account'),
    path('checkout/', views.checkout, name = 'chcekout'),
    path('buy_now/<int:pid>/', views.buy_now, name = 'buy_now'),
    path('my_orders/', views.my_orders, name='my_orders'),
]