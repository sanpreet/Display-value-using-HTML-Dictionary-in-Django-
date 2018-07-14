from django.conf.urls import patterns, include, url
#please add the views file from the application folder and the funtion in the views.py where th eresponse to request is
#contained
from Application_folder.views import index

urlpatterns = patterns('',

    url(r'^',index),

)
