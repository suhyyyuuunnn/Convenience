from django.urls import path
from .views import index, remove, add, show, plus, minus

app_name = "shop"
urlpatterns = [
    path('index/', index, name="index"),
    path('remove/<int:product_id>', remove, name="remove"),
    path('show/', show, name="show"),
    path('add/<int:product_id>', add, name="add"),
    path('plus/<int:product_id>', plus, name="plus"),
    path('minus/<int:product_id>', minus, name="minus"),
]