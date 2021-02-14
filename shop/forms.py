from django import forms
from .models import Product
from django_summernote.widgets import SummernoteWidget


class ProductForm(forms.ModelForm):
    _type = forms.ChoiceField(
        widget=forms.RadioSelect,
        label="게시글 종류",
        choices=Product.SHOP_TYPE,
        required=True
    )

    class Meta:
        model = Product
        fields = ['name', '_type', 'content', 'price']
        labels = {
            'title': '제목',
            'content': '내용',
        }
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control'

            }),
            'content': SummernoteWidget(),
        }
