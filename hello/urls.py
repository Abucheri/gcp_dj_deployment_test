from django.urls import path
from .views import HomePage, AboutPage

urlpatterns = [
	path('about/', AboutPage.as_view(), name='about'),
	path('', HomePage.as_view(), name='home'),
]