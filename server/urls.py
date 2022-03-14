from django.urls import path
from .views import *

urlpatterns = [
    path('alumnis', ViewAlumnis.as_view()),
    path('createalumni', CreateAlumni.as_view()),
    path('updatealumni/<int:registration_no>', UpdateAlumni.as_view()),
    path('updatealumniimage/<int:registration_no>',UpdateAlumniImage.as_view()),

    path("events", ViewEvents.as_view()),
    path("createevent", CreateEvent.as_view()),

    path("hirings",ViewHirings.as_view()),
    path("createhiring", CreateHiring.as_view()),
]
