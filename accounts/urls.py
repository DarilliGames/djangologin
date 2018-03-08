from django.conf.urls import url

from .views import *

urlpatterns = [
    url(r'^$', get_index, name="accounts_index"),
    url(r'^loggin/', login_accounts, name="login"),
    url(r'^register/', register, name="register"),
    url(r'^logout/', logout, name="logout"),
    url(r'^profile/', get_profile, name="profile"),
    
]