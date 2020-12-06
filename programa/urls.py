from django.urls import path
from .views import *

urlpatterns = [
    path('', Index),
    path('cftv-shopping/', Cftv_shopping),
    path('cftv-shopping-create/', Cftv_shopping_create),
    path('cftv-shopping-update/<int:id>', Cftv_shopping_update),
    path('automacao/', Automacao),
    path('sdai-shopping/', Sdai_shopping),
    path('sdai-torre-empresarial/', Sdai_torre_empresarial),

   
]