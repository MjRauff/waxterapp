from django.views import generic
from . import models
from . import forms
from datetime import date as dt
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy

class PlantsListView(LoginRequiredMixin, generic.ListView):
    model = models.Plantprofile
    template_name = "plants/all_plants.html"
    def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            return context


class PlantsDetailView(LoginRequiredMixin, generic.DetailView):
    model = models.Plantprofile
    template_name = "plants/plant_profile.html"

    def post(self, request, slug, pk):
        if request.method == 'POST':
            length = request.POST.get("length", "")
            length = int(length)
            plant = models.Plantprofile.objects.get(pk=pk)
            groth_rate = models.Groth_rate
            groth_rate(plant=plant, length=length).save()
            return redirect("plants:plants_detail", slug=slug, pk= pk)

    def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            plant = models.Plantprofile.objects.get(pk=self.kwargs["pk"])
            dt_water_days = dt.today() - plant.watered
            dt_fertilizer_days = dt.today() - plant.fertilizer
            groth_rate = models.Groth_rate.objects.filter(plant=plant).order_by("date_create")
            context["groth_rate"] = groth_rate
            context["groth_rate_last"] = groth_rate.order_by("date_create", "length").first()
            context["gallery"] = models.Image_profile.objects.filter(plant=plant)
            context["dt_water"] = dt_water_days.days
            context["dt_fertilizer"] = dt_fertilizer_days.days
            return context

class PlantsDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = models.Plantprofile
    template_name = "plants/plant_profile_delete.html"
    success_url = reverse_lazy("plants:plants_list")



class PlantsTypeListView(LoginRequiredMixin, generic.ListView):
    model = models.Plantfamily
    template_name = "plants/all_plants_type.html"

    def post(self, request):
        if request.method == 'POST':
            grab_type = request.POST.get("grab_type", "")
            plant_type = models.Plantfamily.objects.get(name=grab_type)
            new_plant = models.Plantprofile
            new_plant(plant=plant_type).save()
            return redirect("home")

class PlantsTypeDelete(LoginRequiredMixin, generic.DeleteView):
    model = models.Plantfamily
    template_name = "plants\delete_plant_type.html"
    success_url = reverse_lazy("plants:plants_list_type")

class PlantsTypeCreate(LoginRequiredMixin, generic.CreateView):
    form_class = forms.PlantsTypeForm
    success_url = reverse_lazy("plants:plants_list_type")
    template_name = "plants\create_plant_type.html"

class PlantPicCreate(LoginRequiredMixin, generic.CreateView):
    form_class = forms.PlantsPicForm
    template_name = "plants\plant_upload_pic.html"

    def get_success_url(self):
        slug = self.kwargs["slug"]
        pk = self.kwargs["pk"]
        return reverse_lazy('plants:plants_detail', kwargs={'pk': pk, 'slug': slug})

    def form_valid(self, form):
        plant = models.Plantprofile.objects.get(pk=self.kwargs["pk"])
        form.instance.plant = plant
        form.save()
        return super(PlantPicCreate, self).form_valid(form)

class PlantPicDelete(LoginRequiredMixin, generic.DeleteView):
    model = models.Image_profile
    template_name = "plants\delete_plant_type.html"
    def get_success_url(self):
        slug = self.kwargs["slug"]
        pk = self.kwargs["pk2"]
        return reverse_lazy('plants:plants_detail', kwargs={'pk': pk, 'slug': slug})

    def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            object = models.Image_profile.objects.get(pk=self.kwargs["pk"])
            context["test"] = object.image.url
            return context

@login_required
def watered(request, slug, pk):
    plant = models.Plantprofile.objects.get(pk=pk)
    dt_days = dt.today()
    plant.watered = dt_days
    plant.save()
    return redirect("plants:plants_detail", slug=slug, pk=pk)

@login_required
def fertilizer(request, slug, pk):
    plant = models.Plantprofile.objects.get(pk=pk)
    dt_days = dt.today()
    plant.fertilizer = dt_days
    plant.save()
    return redirect("plants:plants_detail", slug=slug, pk=pk)
