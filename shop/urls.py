from django.urls import path
from .import views
app_name='shop'
urlpatterns=[
    path('',views.all_product_category,name="all_product_category"),
    path('<slug:c_slug>/',views.all_product_category,name="product_by_category"),
    path('<slug:c_slug>/<slug:product_slug>/',views.product_details,name="product_details"),
]