from django.contrib.auth import views as auth_views
from django.urls import path
from accounts.views import HomePageView, SignUpView, LoginView, FeedView, IQroomView, SearchView


urlpatterns = [
    path('', HomePageView.as_view(), name='homepage'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('iqfeed/', FeedView.as_view(), name='iqfeed'),
    path('iqroom/', IQroomView.as_view(), name='iqroom'),
    path('search/', SearchView.as_view(), name='search.html')
]
