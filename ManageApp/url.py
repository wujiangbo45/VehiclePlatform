from django.conf.urls import url
import views
urlpatterns = [
    url(r'^$', views.l_list),

    url(r'^1/$', views.test_streaming)
]