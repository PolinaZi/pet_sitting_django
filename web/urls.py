from django.urls import path

from web.views import main_view, registration_view, auth_view, logout_view, pet_edit_view, profile_view

urlpatterns = [
    path("", main_view, name="main"),
    path("registration/", registration_view, name="registration"),
    path("auth/", auth_view, name="auth"),
    path("logout/", logout_view, name="logout"),
    path("pets/add/", pet_edit_view, name="pets_add"),
    path("pets/<int:id>/", pet_edit_view, name="pets_edit"),
    path("profile/", profile_view, name="profile")
]
