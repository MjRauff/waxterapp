from django.urls import path
from . import views

app_name = "plants"

urlpatterns = [
    path("", views.PlantsListView.as_view(), name="plants_list"),
    path('<slug:slug>/<int:pk>', views.PlantsDetailView.as_view(), name='plants_detail'),
    path('<slug:slug>/<int:pk>/delete', views.PlantsDeleteView.as_view(), name='plants_delete'),
    path('<slug:slug>/<int:pk>/#watered', views.watered, name='watered'),
    path('<slug:slug>/<int:pk>/#fertilizer', views.fertilizer, name='fertilizer'),
    path("family", views.PlantsTypeListView.as_view(), name="plants_list_type"),
    path("family/<slug:slug>/delete", views.PlantsTypeDelete.as_view(), name="delete_type"),
    path("family/create", views.PlantsTypeCreate.as_view(), name="create_type"),
    path("<slug:slug>/<int:pk>/upload-image", views.PlantPicCreate.as_view(), name="upload_pic"),
    path("<slug:slug>/<int:pk>/<int:pk2>/delete-image", views.PlantPicDelete.as_view(), name="delete_pic"),
]
