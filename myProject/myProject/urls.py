from django.contrib import admin
from django.urls import path
from myProject.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', signupPage,name='signupPage'),
    path('signinPage', signinPage,name='signinPage'),
    path('myDashboard', myDashboard,name='myDashboard'),
    path('logoutpage', logoutpage,name='logoutpage'),

    path('teacherHome', teacherHome,name='teacherHome'),
    path('teacherAdd', teacherAdd,name='teacherAdd'),
    path('teacherDelete/<str:myid>', teacherDelete,name='teacherDelete'),
    path('teacherEdit/<str:myid>', teacherEdit,name='teacherEdit'),

    path('studentHome', studentHome,name='studentHome'),
    path('studentAdd', studentAdd,name='studentAdd'),
    path('studentDelete/<str:myid>', studentDelete,name='studentDelete'),
    path('studentEdit/<str:myid>', studentEdit,name='studentEdit'),

    path('staffHome', staffHome,name='staffHome'),
    path('staffAdd', staffAdd,name='staffAdd'),
    path('staffDelete/<str:myid>', staffDelete,name='staffDelete'),
    path('staffEdit/<str:myid>', staffEdit,name='staffEdit'),

    path('doctorHome', doctorHome,name='doctorHome'),
    path('doctorAdd', doctorAdd,name='doctorAdd'),
    path('doctorDelete/<str:myid>', doctorDelete,name='doctorDelete'),
    path('doctorEdit/<str:myid>', doctorEdit,name='doctorEdit'),

    path('nurseHome', nurseHome,name='nurseHome'),
    path('nurseAdd', nurseAdd,name='nurseAdd'),
    path('nurseDelete/<str:myid>', nurseDelete,name='nurseDelete'),
    path('nurseEdit/<str:myid>', nurseEdit,name='nurseEdit'),

    path('employeeHome', employeeHome,name='employeeHome'),
    path('employeeAdd', employeeAdd,name='employeeAdd'),
    path('employeeDelete/<str:myid>', employeeDelete,name='employeeDelete'),
    path('employeeEdit/<str:myid>', employeeEdit,name='employeeEdit'),
]
