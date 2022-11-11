from django.forms import ModelForm
from .models import Contact

class ContactForm(ModelForm):
    model = Contact
    fields = '__all__'
    
