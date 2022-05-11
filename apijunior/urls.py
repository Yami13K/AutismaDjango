from django.urls import path
from .views import Record, cLogin, Login, Logout,Addchild,Addimage,Addgame

urlpatterns = [
    path('register/', Record.as_view(), name="register"),
    path('login/', Login.as_view(), name="login"),
    path('clogin/', cLogin.as_view(), name="clogin"),
    path('logout/', Logout.as_view(), name="logout"),
    path('signup/', Addchild.as_view(), name="signup"),
    path('uploadimage/', Addimage.as_view(), name="uploadimage"),
    path('game/', Addgame.as_view(), name="game"),
   

]