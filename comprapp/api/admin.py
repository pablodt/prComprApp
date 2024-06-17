from django.contrib import admin
from .models import PurchasingUser, House, Membership, SuperMarket, Product

# Register your models here.

admin.site.register(PurchasingUser)
admin.site.register(House)
admin.site.register(Membership)
admin.site.register(SuperMarket)
admin.site.register(Product)