from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    #Main page
    path("",views.indexpage,name="index"),
    path("login",views.login,name="login"),
    path("joinus",views.joinus,name="joinus"),
    path("checkuserlogin",views.checkuserlogin,name="checkuserlogin"),
    path("joinussucc",views.joinussucc,name="joinussucc"),
    path("home", views.home, name="home"),

    #user
    path("userhome", views.userhome, name="userhome"),
    path("userlogout", views.userlogout, name="userlogout"),

    #Admin
    path("adminlogin", views.adminlogin, name="adminlogin"),
    path("adminhome", views.adminhome, name="adminhome"),
    path("checkadminlogin",views.checkadminlogin,name="checkadminlogin"),



    #demo
    path("addcar", views.addcar, name="addcar"),
    path("viewallcars", views.viewallcars, name="viewallcars"),
    path("displayallcars", views.displayallcars, name="displayallcars"),

    path("addproduct", views.addproduct, name="addproduct"),
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)