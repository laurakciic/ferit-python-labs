from .models import Image, Comment
from django.forms import ModelForm, widgets
from bootstrap_datepicker_plus import DateTimePickerInput
class ImageForm(ModelForm):
    class Meta:
        model = Image
        fields = ['title', 'url', 'description', 'pub_date']
        widgets = {
            'pub_date': DateTimePickerInput()
        }
class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['text']