from django.urls import path 
from chatbot import views
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve

urlpatterns = [
	path('', views.index, name='chatbot'),
	path('update/<int:id>', views.update, name='update'),
	path('delete/<int:id>', views.delete, name='delete'),

	path('res', views.indexresp, name='chatbotresp'),
	path('updateres/<int:id>', views.updateresp, name='updateresp'),
	path('deleteres/<int:id>', views.deleteresp, name='deleteresp'),
]