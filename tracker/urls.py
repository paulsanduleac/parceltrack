from django.urls import path

from . import views

app_name = 'tracker'

urlpatterns = [
    path('', views.index, name='index'),
    # the 'name' value as called by the {% url %} template tag
    path('<int:parcel_id>/', views.parcel_detail, name='parcel_detail')
]