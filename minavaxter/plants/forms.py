from django.forms import ModelForm
from . import models

class PlantsTypeForm(ModelForm):
    class Meta:
        model = models.Plantfamily
        fields = ["name", "species", "light", "light_details", "water", "water_details", "info", "link"]

class PlantsPicForm(ModelForm):
    class Meta:
        model = models.Image_profile
        fields = ["image",]
    def __init__(self, *args, **kwargs):
        super(PlantsPicForm, self).__init__(*args, **kwargs)
        self.fields['image'].required = True
