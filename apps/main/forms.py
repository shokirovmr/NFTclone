from apps.main.models import Product
from apps.users import forms


class ProductCreateForm(forms.ModelForm):
    def init(self, *args, **kwargs):
        super().init(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs.update(
                    {"class": "form-control", "placeholder": f"Enter the {str(field)}"})

    class Meta:
        model = Product
        fields = ("title", "description", "price", 'category','ends_in','owner', 'image')


class ProductUpdateForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ("title", "description", "price", 'category','ends_in','owner', 'image')