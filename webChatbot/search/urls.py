from django.urls import path
from . import views

app_name = 'search'

urlpatterns = [
	path('chatbot/', views.search, name='search'),
	path('chatbot/res/', views.searchr, name='searchr'),
]
