from django.conf import settings
from rest_framework.routers import DefaultRouter
from rest_framework.routers import SimpleRouter

from spm_task.users.api.views import UserViewSet
from spm_task.company.api.views import CompanyView
from spm_task.client.api.views import ClientView
router = DefaultRouter() if settings.DEBUG else SimpleRouter()

router.register("users", UserViewSet)
router.register("comapnies", CompanyView)
router.register("clients", ClientView)


app_name = "api"
urlpatterns = router.urls
