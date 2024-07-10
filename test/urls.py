from django.urls import path
from .views import MembersRegistrationAPIView, MembersActivationAPIView, ActiveMembersListView

urlpatterns = [
    path('register/', MembersRegistrationAPIView.as_view(), name='member-registration'),
    path('activate/', MembersActivationAPIView.as_view(), name='member-activation'),
    path('list_members/', ActiveMembersListView.as_view(), name='active-members-list')
]