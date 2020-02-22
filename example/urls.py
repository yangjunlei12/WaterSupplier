from django.urls import path
import example.views as views

urlpatterns = [
    path('mk/', views.get_example)
]