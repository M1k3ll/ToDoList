from django.urls import include, path
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('',views.TodoViewSetApiView)



urlpatterns =[

        path('',views.all_todos),
        path('viewsets/',include(router.urls)),
        path('users/', views.UsersGenericApiview.as_view()),



]