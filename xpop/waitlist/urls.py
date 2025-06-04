from django.urls import path
from . import views

app_name = 'waitlist'

urlpatterns = [
    # Main landing page view
    path('', views.LandingPageView.as_view(), name='landing'),
    

    # Alternative simple API (non-DRF)
    path('api/waitlist/', views.simple_waitlist_api, name='simple_waitlist'),
]