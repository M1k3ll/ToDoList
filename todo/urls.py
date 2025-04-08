from django.urls import include, path
from . import views
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()
router.register('',views.TodoViewSetApiView)



urlpatterns = [

        path('', views.all_todos),
        path('viewsets/', include(router.urls)),
        path('users/', views.UsersGenericApiview.as_view()),
        path('api/token/', obtain_auth_token, name='api_token_auth'),

]
