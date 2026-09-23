from django.urls import path
from .views import AuditoriaListView

urlpatterns = [
    path('registros/', AuditoriaListView.as_view(), name='lista_auditoria'),
]