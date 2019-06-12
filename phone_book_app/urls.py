from django.urls import path
from . import views

urlpatterns = [
    path('', views.OsobaListView.as_view()),
    path('<int:pk>/', views.OsobaDetailView.as_view(), name='detail'),
]
