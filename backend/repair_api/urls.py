# repair_api/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from . import views

router = DefaultRouter()
router.register(r'categories', views.EquipmentCategoryViewSet, basename='category')
router.register(r'equipment', views.EquipmentViewSet, basename='equipment')
router.register(r'repair-requests', views.RepairRequestViewSet, basename='repair-request')
router.register(r'profiles', views.UserProfileViewSet, basename='profile')
router.register(r'auth', views.RegisterView, basename='auth')

urlpatterns = [
    # JWT Authentication
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # Custom endpoints
    path('dashboard/stats/', views.dashboard_stats, name='dashboard_stats'),
    path('technicians/', views.technician_list, name='technician_list'),

    # Router endpoints
    path('', include(router.urls)),
]

# Swagger (optional)
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Repair System API",
        default_version='v1',
        description="ระบบบริหารจัดการคำร้องขอซ่อม",
        contact=openapi.Contact(email="admin@example.com"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns += [
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
