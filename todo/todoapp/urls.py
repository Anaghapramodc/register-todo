from django.urls import path

from .views import RegisterView, RegistrationDetailView, TaskUpdate

urlpatterns = [
    path('create', RegisterView.as_view(), name='task-create'),
    path('registrationview/<int:pk>/', RegistrationDetailView.as_view(), name='registration-detail'),
    path('update/<int:pk>/', TaskUpdate.as_view(), name='task-update'),

]

