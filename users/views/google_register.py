import requests
from django.urls import reverse
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from social_core.exceptions import MissingBackend
from social_django.utils import load_strategy, load_backend

from root.settings import SOCIAL_AUTH_GOOGLE_OAUTH2_KEY, SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET


class GoogleAuthView(APIView):
    permission_classes = [AllowAny]

    @classmethod
    def get(cls, request):
        # Build the redirect URI for the Google authentication callback
        redirect_uri = request.build_absolute_uri(reverse('google-auth-callback'))
        # Load the strategy and backend for Google OAuth2
        strategy = load_strategy(request)
        backend = load_backend(strategy, 'google-oauth2', redirect_uri=redirect_uri)
        # Get the authorization URL
        authorize_url = backend.auth_url()
        return Response({'authorize_url': authorize_url})


class GoogleAuthCallbackView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        # Get the authorization code from the request query parameters
        authorization_code = request.GET.get('code')
        # Build the redirect URI for the Google authentication callback
        redirect_uri = request.build_absolute_uri(reverse('google-auth-callback'))
        # Get the backend for Google OAuth2
        backend = self.get_backend(request)

        if not authorization_code or not backend:
            return Response(status=400)

        # URL for exchanging authorization code for access token
        token_url = 'https://accounts.google.com/o/oauth2/token'

        # Data to be sent in the token exchange request
        data = {
            'code': authorization_code,
            'redirect_uri': redirect_uri,
            'client_id': SOCIAL_AUTH_GOOGLE_OAUTH2_KEY,
            'client_secret': SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET,
            'grant_type': 'authorization_code',
        }

        # Perform the token exchange request
        response = requests.post(token_url, data=data)
        if response.status_code == 200:
            # Extract the access token from the response
            access_token = response.json().get('access_token')
        else:
            return Response({'error': 'Failed to exchange authorization code for access token'}, status=400)

        if access_token:
            # Authenticate the user using the access token
            user = backend.do_auth(access_token)
            if user:
                # Generate JWT tokens for the authenticated user
                refresh = RefreshToken.for_user(user)
                access_token = str(refresh.access_token)
                refresh_token = str(refresh)
                return Response({'access_token': access_token, 'refresh_token': refresh_token}, status=200)

        return Response(status=400)

    @staticmethod
    def get_backend(request):
        strategy = load_strategy(request)
        try:
            return load_backend(strategy, 'google-oauth2', redirect_uri=None)
        except MissingBackend:
            return None
