from django.contrib import admin
from django.urls import reverse
from django.utils.html import escape, mark_safe
from . import models


class ProductImagesInline(admin.StackedInline):
    model = models.ProductImages
    extra = 1


class RelatedProductInline(admin.StackedInline):
    model = models.RelatedProduct
    extra = 1
    fk_name = 'prod'


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'rating', 'sub_name']
    search_fields = ['name',]
    inlines = [ProductImagesInline, RelatedProductInline]


class EmailNewsAdmin(admin.ModelAdmin):
    list_display = ['subject', 'body']


class ContactUsCommentAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'message', 'read']
    list_filter = ['read',]

    def has_add_permission(self, request, obj=None):
        return False


class QuestionAdmin(admin.ModelAdmin):
    list_display = ['product', 'question', 'answer', 'date_time', 'read']
    list_filter = ['read',]

    def has_add_permission(self, request, obj=None):
        return False


class DistributorAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'short_message', 'read']
    list_filter = ['read',]

    def has_add_permission(self, request, obj=None):
        return False


class ProductListInline(admin.TabularInline):
    model = models.ProductList
    readonly_fields = ['product', 'price', 'quantity', 'sub_total']
    can_delete = False
    extra = 0

    def sub_total(self, obj):
        return obj.price * obj.quantity

    def has_add_permission(self, request, obj):
        return False


class OrderAdmin(admin.ModelAdmin):
    list_display = ['get_name', 'oid', 'status', 'order_date_time', 'get_city', 'get_state']
    list_filter = ['order_date_time', 'status']
    inlines = [ProductListInline,]
    readonly_fields = ['user', 'first_name', 'last_name', 'address', 'phone', 'city', 'state', 'pin_code', 'total', 'payment_status', 'oid']
    search_fields = ['oid']

    # def link_to_user(self, obj: models.Order):
    #     link = reverse('admin:module_model_change', args=[obj.model_id])
    #     return mark_safe(f'<a href="{link}">{escape(obj.model.__str__())}</a>')

    # todo, uncomment previous function before production
    # def get_queryset(self, request):
    #     qs = super().get_queryset(request)
    #     return qs.filter(payment_status = '2')

    def has_add_permission(self, request, obj=None):
        return False

    def get_name(self, obj):
        return obj.first_name+' '+obj.last_name

    def get_city(self, obj):
        return obj.city

    def get_state(self, obj):
        return obj.state


class NewsLetterSubscriberAdmin(admin.ModelAdmin):

    def has_add_permission(self, request, obj=None):
        return False


admin.site.register(models.Product, ProductAdmin)
admin.site.register(models.Question, QuestionAdmin)
admin.site.register(models.Order, OrderAdmin)
admin.site.register(models.NewsLetterSubscriber, NewsLetterSubscriberAdmin)
admin.site.register(models.EmailNews, EmailNewsAdmin)
admin.site.register(models.ContactUsComment, ContactUsCommentAdmin)
admin.site.register(models.Distributor, DistributorAdmin)