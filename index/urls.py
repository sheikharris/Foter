from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static 
urlpatterns = [
    path('', views.index,name="index"),
    path('About_Foter',views.About_Foter,name="About_Foter"),
    path('Contact_us',views.Contact_us,name="Contact_us"),
    path('signup',views.signup,name="signup"),
    path('login',views.login,name="login"),
    path('logout',views.logout,name="logout"),
    path('rcfood',views.rcfood,name="rcfood")
]

urlpatterns=urlpatterns+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
