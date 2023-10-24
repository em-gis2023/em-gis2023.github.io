from django.urls import path
from . import views

urlpatterns = [
    path('index', views.toIndex_view),
    path('committee', views.toCommittee_view),
    path('program', views.toProgram_view),
    path('submission', views.toSubmission_view),
    path('program/2023', views.toProgram2023_view),

]


