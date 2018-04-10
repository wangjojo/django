from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.get_blogs,name = 'get_blog'),
    url(r'^detail/(\d+)/$',views.get_details,name = 'blog_get_detail'),
]