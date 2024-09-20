from django.urls import path
from . import views

urlpatterns = [
    path('submitData/<int:id>/', views.get_pereval_by_id, name='get_pereval_by_id'),
    path('submitData/<int:id>/update/', views.update_pereval, name='update_pereval'),
    path('submitData/', views.get_perevals_by_user_email, name='get_perevals_by_user_email'),
]
