from django.urls import path
from .views import *

urlpatterns = [
    path('cybersport/', CyberSportRegistrationAPIView.as_view()),
    path('hackathon/', HackathonRegistrationAPIView.as_view()),
    path('design/', DesignRegistrationAPIView.as_view()),
    path('mobilography/', MobilographyRegistrationAPIView.as_view()),
    path('robotix/', RobotixRegistrationAPIView.as_view()),
    path('dronerace/', DroneRaceRegistrationAPIView.as_view()),
    path('speaker/', SpeakerRegistrationAPIView.as_view()),
    path('masterclass/', MasterClassRegistrationAPIView.as_view())
]