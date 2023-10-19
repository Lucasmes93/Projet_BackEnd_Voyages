from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Voyage",
        default_version='v1',
        description="L'API permet aux utilisateurs de recevoir des recommandations de voyage personnalisées en "
                    "fonction de leurs préférences, de leur budget et de leur emplacement actuel. Elle peut être "
                    "utilisée par des applications mobiles, des sites web de voyage ou d'autres services liés au "
                    "voyage.",

    ),
    public=True,
    permission_classes=(permissions.AllowAny,),  # Cela permet à tout le monde d'accéder à la documentation.
)
