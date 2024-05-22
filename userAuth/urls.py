from django.urls import path, include
from dj_rest_auth.views import LoginView, LogoutView ,UserDetailsView
from dj_rest_auth.registration.views import RegisterView


urlpatterns = [
    
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('registration/', include('dj_rest_auth.registration.urls')),
    path('user/',UserDetailsView.as_view(),name='user'),
    path('', include('dj_rest_auth.urls')),  # Includes other dj-rest-auth endpoints
]