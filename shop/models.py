from django.db import models
from django.urls import reverse
from django_summernote.utils import get_attachment_storage, get_attachment_upload_to
from carton.cart import Cart


class Product(models.Model):
    class Meta:
        ordering = ['-updated_at']

    SHOP_TYPE = [
        (0, "7eleven"),
        (1, "CU"),
        (2, "GS25")
    ]

    name = models.CharField(max_length=200, verbose_name="상품명")
    content = models.TextField()
    image = models.ImageField(upload_to="shop/img", blank=True,
                              default="shop/default/default.jpg", verbose_name="대표 이미지")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="등록시간")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="업데이트시간")
    _type = models.PositiveSmallIntegerField(choices=SHOP_TYPE, verbose_name="상호명")
    price = models.IntegerField(default=0, verbose_name="가격")

    def value(self):
        return self._type

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:show-cart', args=[self.pk])
