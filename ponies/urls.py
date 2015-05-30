"""ponies URL Configuration
"""
from django.conf.urls import include, url
from django.contrib import admin
from conferences import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.index, name="index"),
    url(r'^conferences$', views.view_conferences, name="view_conferences"),
    url(r'^conferences.json$', views.view_conferences_json, name="view_conferences_json"),
]
