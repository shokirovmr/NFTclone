from django.contrib import admin

from apps.main.models import ProductLike


# Register your models here.




@admin.register(ProductLike)
class ProductLikeAdmin(admin.ModelAdmin):
    pass