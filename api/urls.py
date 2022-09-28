from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView
from api.models import User,UserProfile, Product



urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]


from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register("product", views.ProductAPIView)
router.register("register", views.SignupView)

app_name = "api"
urlpatterns = router.urls + urlpatterns






























