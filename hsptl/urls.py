from django.urls import path
from.import views
urlpatterns = [
    path("hello",views.HELLO,name="newone"),
    path("hsptl",views.hello,name="login"),
    path("hai",views.hai,name="new"),
    path("newpage",views.newpage,name='page')
]