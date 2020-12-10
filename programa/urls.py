from django.urls import path
from .views import *
from django.contrib.auth import views

urlpatterns = [
    path('login/', views.LoginView.as_view(template_name='login.html'), name="login"),
    path('logout/', views.LogoutView.as_view(), name="logout"),

    path('', Index),
    path('cftv-shopping/', Cftv_shopping),
    path('cftv-shopping-create/', Cftv_shopping_create),
    path('cftv-shopping-update/<int:id>', Cftv_shopping_update),
    path('automacao/', Automacao),
    path('automacao-update/<int:id>', AutomacaoUpdate),
    path('sdai-shopping/', Sdai_shopping),
    path('sdai-torre-empresarial/', Sdai_torre_empresarial),

   
]