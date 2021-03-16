from django.urls import path
from . import views

app_name = "Core"
urlpatterns = [
    path('polls/', views.PollViewSet.as_view({'get': 'list'})),
    path('polls/<int:pk>/', views.PollViewSet.as_view({'get': 'retrieve'})),
]
