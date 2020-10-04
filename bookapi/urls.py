from bookapi import views

from rest_framework import routers

app_name = 'bookapi'

router = routers.SimpleRouter()
router.register('books', views.BookViewSet)

urlpatterns = router.urls
