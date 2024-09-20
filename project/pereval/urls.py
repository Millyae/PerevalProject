from django.urls import path
from .views import submitData

urlpatterns = [
    path('submit/', submitData, name='submit_data'),
]
