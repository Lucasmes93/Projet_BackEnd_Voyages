# recommendations/urls.py
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from voyages.swagger import schema_view
from voyages.recommendations.views import UserProfileViewSet, DestinationViewSet, BookingViewSet

# Créez un routeur pour générer automatiquement les URLs pour les vues de l'API.
router = DefaultRouter()
router.register(r'userprofile', UserProfileViewSet)
router.register(r'destinations', DestinationViewSet)
router.register(r'bookings', BookingViewSet)


urlpatterns = [
    # Incluez les URLs générées par le routeur dans le chemin racine de l'API.
    
    path('api/', include(router.urls)),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    ##re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
