from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ContactViewSet, PhoneViewSet, EmailViewSet, AddressViewSet

router = DefaultRouter()
router.register(r'contacts', ContactViewSet)
router.register(r'phones', PhoneViewSet)
router.register(r'emails', EmailViewSet)
router.register(r'addresses', AddressViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('contacts/<int:pk>/profile_image/', ContactViewSet.as_view({'get': 'profile_image'})),
]