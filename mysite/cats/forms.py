from django.forms import ModelForm
from .models import Cat, Breed


# Create the form class.
class CatForm(ModelForm):
    class Meta:
        model = Cat
        fields = '__all__'
    
class BreedForm(ModelForm):
    class Meta:
        model = Breed
        fields = '__all__'