from django.urls import path
from . import views
urlpatterns = [
    path('properties', views.load_all_data),
    path('property/<int:property_id>/', views.property_detail),
    path('reservation', views.create_reservation),
    path('newsletter', views.newsletter),
    path('customer_message', views.customer_message),
]
