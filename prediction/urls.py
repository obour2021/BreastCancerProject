from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.PredictCreate, name='home'),
    path('predictionlist/', views.PredictionList.as_view(), name='dashboard'),
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('account/', include("django.contrib.auth.urls"))
]
