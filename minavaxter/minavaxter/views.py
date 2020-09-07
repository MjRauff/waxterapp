from django.views import generic
from django.shortcuts import render, redirect

class IndexView(generic.TemplateView):
    def get(self, request):
        return redirect("plants:plants_list")
