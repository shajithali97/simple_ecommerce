from django.contrib import admin
from . models import Category,Product

class CategoryAdmin(admin.ModelAdmin):
    list_display=['category_name','slug']
    prepopulated_fields={'slug':('category_name',)}
admin.site.register(Category,CategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display=['product_name','price','stock','available','created','updated']
    list_editable=['price','stock','available']
    prepopulated_fields={'slug':('product_name',)}
    list_per_page=20
admin.site.register(Product,ProductAdmin)
