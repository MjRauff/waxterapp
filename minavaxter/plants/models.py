from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.forms import ModelForm
# Create your models here.
ICON_CHOICES = [
    ("MISSING_DATA", "Missing Data"),
    ("LOW", "Low"),
    ("MEDIUM", "Medium"),
    ("HIGH", "High"),
]

class Plantfamily(models.Model):
    name = models.CharField(max_length=100, blank=True)
    slug = models.SlugField(allow_unicode=True, unique=True, blank=True)
    species = models.CharField(max_length=100, blank=True)
    light = models.CharField(max_length=100, choices=ICON_CHOICES, default="MISSING_DATA")
    light_details = models.TextField(max_length=2000, blank=True)
    water = models.CharField(max_length=100, choices=ICON_CHOICES, default="MISSING_DATA")
    water_details = models.TextField(max_length=2000, blank=True)
    info = models.TextField(max_length=2000, blank=True)
    link = models.URLField(max_length=1000, blank=True)
    date_create = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    def light_color(self):
        if self.light == "LOW":
            return "text-danger"
        elif self.light == "MEDIUM":
            return "text-warning"
        elif self.light == "HIGH":
            return "text-success"
        else:
            print("Error Color Light")
    def water_color(self):
        if self.water == "LOW":
            return "text-danger"
        elif self.water == "MEDIUM":
            return "text-warning"
        elif self.water == "HIGH":
            return "text-success"
        else:
            print("Error Color Water")
    def __str__(self):
        return self.name
    def profile_pic(self):
        image = Image_profile.objects.filter(plant=self)
        return image.order_by("-date_create").first()
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)
    class Meta:
        ordering = ("name", "date_create",)

class Plantprofile(models.Model):
    plant = models.ForeignKey(Plantfamily,  on_delete=models.CASCADE, blank=True, null=True)
    watered = models.DateField(null=True, blank=True, default="2000-01-01")
    fertilizer = models.DateField(null=True, blank=True, default="2000-01-01")
    kia = models.BooleanField(default=False)
    date_create = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    def __str__(self):
        return "{} ( {} )".format(self.plant.name, self.pk)
    def profile_pic(self):
        image = Image_profile.objects.filter(plant=self)
        return image.order_by("-date_create").first()
    def length(self):
        object = Groth_rate.objects.filter(plant=self).first()
        try:
            return object.length
        except:
            return "???"
    class Meta:
        ordering = ("plant", "date_create",)

class Image_profile(models.Model):
    plant = models.ForeignKey(Plantprofile, on_delete=models.CASCADE, blank=True, null=True)
    image = models.ImageField(upload_to="plants/", blank=True, null=True)
    date_create = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return "{} {}".format(self.plant, self.date_create.strftime('%B %d %Y'))
    class Meta:
        ordering = ("date_create","plant",)

class Groth_rate(models.Model):
    plant = models.ForeignKey(Plantprofile, on_delete=models.CASCADE, blank=True, null=True)
    length = models.IntegerField(default=0)
    date_create = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return "{} {}".format(self.plant, self.date_create.strftime('%B %d %Y'))
    class Meta:
        ordering = ("-date_create","plant",)
