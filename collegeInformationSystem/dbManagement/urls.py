
from django.urls import path
from . import views
# from .filters import StudentFilter

urlpatterns = [
   path('log/', views.login_user,name= "login"),
   path('search/', views.search_details, name = "search")
]
