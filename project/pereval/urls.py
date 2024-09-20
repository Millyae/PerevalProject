from django.urls import path, re_path
from rest_framework import permissions
from rest_framework.schemas import get_schema_view, openapi
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from . import views

schema_view = get_schema_view(
    openapi.Info(
        title="Pereval API",
        default_version='v1',
        description="Документация API для проекта Pereval",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@pereval.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('submitData/<int:id>/', views.get_pereval_by_id, name='get_pereval_by_id'),
    path('submitData/<int:id>/update/', views.update_pereval, name='update_pereval'),
    path('submitData/', views.get_perevals_by_user_email, name='get_perevals_by_user_email'),

    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]