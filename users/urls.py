from django.urls import path

from users.views import GoogleAuthView, GoogleAuthCallbackView

# Define URL patterns for user authentication using Google OAuth2
urlpatterns = [
    # Endpoint for initiating the Google OAuth2 authentication process
    path('login/google-oauth2/', GoogleAuthView.as_view(), name='google-auth'),

    # Endpoint for handling the callback from Google OAuth2 after authentication
    path('complete/google-oauth2/', GoogleAuthCallbackView.as_view(), name='google-auth-callback')
]
